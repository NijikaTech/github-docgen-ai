import httpx
from typing import Dict, Any

class DocGenerator:
    def __init__(self, config: dict):
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.base_url = config['llm']['base_url']

    async def generate_readme(self, repo_name: str, file_tree_summary: str) -> str:
        prompt = f"""
You are an expert technical writer. Generate a comprehensive, professional README.md for the GitHub repository named '{repo_name}'.

Here is the repository file structure:
{file_tree_summary}

Structure the README with the following sections:
1. **Title & Short Description**
2. **Key Features**
3. **Project Structure**
4. **Getting Started & Installation**
5. **Usage Guide**

Keep it concise, clear, and cleanly formatted in Markdown.
"""
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json().get("response", "")