import asyncio
import os
import yaml
from dotenv import load_dotenv
import typer
from rich.console import Console
from rich.panel import Panel

from src.github_client import GitHubClient
from src.parser import RepoParser
from src.doc_generator import DocGenerator

load_dotenv()
app = typer.Typer()
console = Console()

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

@app.command()
def generate(repo: str = typer.Argument(..., help="Repository in 'owner/repo' format (e.g. NijikaTech/github-docgen-ai)")):
    """
    Generate a README.md for any public GitHub repo using Ollama locally.
    """
    if "/" not in repo:
        console.print("[bold red]Error:[/bold red] Repo must be formatted as 'owner/repo'")
        raise typer.Exit(code=1)

    owner, repo_name = repo.split("/")
    config = load_config()
    github_token = os.getenv("GITHUB_TOKEN")

    async def run():
        console.print(Panel(f"[bold green]Analyzing {owner}/{repo_name}...[/bold green]"))
        
        # 1. Fetch
        client = GitHubClient(token=github_token)
        tree = await client.fetch_repo_structure(owner, repo_name)
        
        # 2. Parse
        parser = RepoParser(config)
        filtered_tree = parser.filter_tree(tree)
        tree_summary = parser.build_tree_summary(filtered_tree)
        
        console.print(f"[dim]Found {len(filtered_tree)} relevant files.[/dim]")
        console.print("[yellow]Generating README with Ollama...[/yellow]")
        
        # 3. Generate
        generator = DocGenerator(config)
        readme_content = await generator.generate_readme(repo_name, tree_summary)
        
        # Save output
        os.makedirs("output", exist_ok=True)
        output_path = os.path.join("output", f"{repo_name}_README.md")
        with open(output_path, "w") as f:
            f.write(readme_content)
            
        console.print(f"[bold green]Successfully generated README![/bold green] Saved to: [bold]{output_path}[/bold]")

    asyncio.run(run())

if __name__ == "__main__":
    app()