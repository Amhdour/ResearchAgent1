"""
Summarizer Agent - Information Synthesis

Role: Cognition Layer
Responsibility: Processes and condenses information from multiple sources

Educational Concept:
The Summarizer demonstrates 'information fusion' - combining data from
multiple sources into coherent knowledge. This is crucial in Agentic AI
for transforming raw data into actionable insights.
"""

from typing import List, Dict, Any
from datetime import datetime


class SummarizerAgent:
    """
    Synthesizes information from multiple sources into coherent summaries.
    
    Agentic AI Principle: Information Fusion & Synthesis
    - Combines data from disparate sources
    - Identifies key themes and patterns
    - Reduces information overload
    - Maintains source attribution
    """
    
    def __init__(self, knowledge_graph=None):
        """
        Initialize the Summarizer Agent.
        
        Args:
            knowledge_graph: Reference to the knowledge graph for logging
        """
        self.knowledge_graph = knowledge_graph
        self.name = "SummarizerAgent"
    
    def summarize(self, search_results: List[List[Dict[str, Any]]]) -> Dict[str, Any]:
        """
        Synthesize multiple search results into a structured summary.
        
        Args:
            search_results: List of search result lists from different queries
            
        Returns:
            Structured summary with key findings and sources
            
        Educational Note:
        In production, this would use LLM-based summarization (e.g., via GroqCloud).
        The LLM would:
        - Extract key concepts across sources
        - Identify agreements and contradictions
        - Generate coherent narrative summaries
        - Maintain factual accuracy with citations
        """
        self._log_action("summarization_started", {
            "source_count": len(search_results)
        })
        
        summary = self._synthesize_information(search_results)
        
        self._log_action("summarization_completed", {
            "source_count": len(search_results),
            "key_points": len(summary.get("key_findings", []))
        })
        
        return summary
    
    def _synthesize_information(self, search_results: List[List[Dict[str, Any]]]) -> Dict[str, Any]:
        """
        Combine and structure information from multiple sources.
        
        Educational Note:
        This heuristic implementation demonstrates the pattern.
        Real implementation would use:
        - LLM-based extraction of key concepts
        - Semantic similarity to group related information
        - Citation tracking for source attribution
        - Fact-checking across multiple sources
        """
        all_results = []
        for result_list in search_results:
            all_results.extend(result_list)
        
        key_findings = []
        sources = []
        
        for result in all_results[:10]:
            key_findings.append({
                "point": result.get("snippet", "")[:200],
                "source": result.get("title", "Unknown"),
                "url": result.get("url", "")
            })
            
            if result.get("url"):
                sources.append({
                    "title": result.get("title", "Unknown"),
                    "url": result.get("url", "")
                })
        
        summary = {
            "key_findings": key_findings,
            "source_count": len(all_results),
            "sources": sources[:15],
            "synthesis_method": "heuristic_extraction"
        }
        
        return summary
    
    def _log_action(self, action: str, data: Dict[str, Any]):
        """Log summarization actions to knowledge graph."""
        if self.knowledge_graph:
            self.knowledge_graph.log_agent_action(
                agent=self.name,
                action=action,
                data=data,
                timestamp=datetime.now().isoformat()
            )
