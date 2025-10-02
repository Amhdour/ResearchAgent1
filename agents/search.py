"""
Search Agent - Information Retrieval

Role: Perception Layer
Responsibility: Gathers information from external sources (web, APIs, databases)

Educational Concept:
The Search Agent represents the 'perception' component of Agentic AI.
Just as humans perceive the world through senses, AI agents perceive through
tools like web search, APIs, and databases. This agent demonstrates how
autonomous systems interact with external knowledge sources.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS
import time


class SearchAgent:
    """
    Searches for information using web APIs and other sources.
    
    Agentic AI Principle: Tool Use & External Perception
    - Interacts with external systems autonomously
    - Handles errors and retries gracefully
    - Structures unstructured web data for downstream processing
    """
    
    def __init__(self, knowledge_graph=None):
        """
        Initialize the Search Agent.
        
        Args:
            knowledge_graph: Reference to the knowledge graph for logging
        """
        self.knowledge_graph = knowledge_graph
        self.name = "SearchAgent"
        self.max_results = 5
    
    def search(self, query: str, max_results: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Execute a web search and return structured results.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of search results with title, snippet, and URL
            
        Educational Note:
        This demonstrates autonomous tool use - the agent decides how to
        query external systems and handle their responses without human intervention.
        """
        max_results = max_results or self.max_results
        
        self._log_action("search_started", {"query": query})
        
        try:
            results = self._execute_search(query, max_results)
            
            self._log_action("search_completed", {
                "query": query,
                "result_count": len(results),
                "success": True
            })
            
            return results
            
        except Exception as e:
            self._log_action("search_failed", {
                "query": query,
                "error": str(e)
            })
            return []
    
    def _execute_search(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """
        Execute DuckDuckGo search.
        
        Educational Note:
        Using DuckDuckGo because it doesn't require API keys, making this
        educational example accessible to everyone. In production, you might use:
        - Google Custom Search API
        - Bing Search API
        - Specialized academic databases (arXiv, PubMed)
        - Internal knowledge bases
        """
        results = []
        
        try:
            with DDGS() as ddgs:
                search_results = ddgs.text(query, max_results=max_results)
                
                for idx, result in enumerate(search_results):
                    results.append({
                        "rank": idx + 1,
                        "title": result.get("title", "No title"),
                        "snippet": result.get("body", "No description"),
                        "url": result.get("href", ""),
                        "source": "duckduckgo"
                    })
                    
                    time.sleep(0.5)
                    
        except Exception as e:
            print(f"Search error: {e}")
        
        return results
    
    def _log_action(self, action: str, data: Dict[str, Any]):
        """Log search actions to knowledge graph."""
        if self.knowledge_graph:
            self.knowledge_graph.log_agent_action(
                agent=self.name,
                action=action,
                data=data,
                timestamp=datetime.now().isoformat()
            )
