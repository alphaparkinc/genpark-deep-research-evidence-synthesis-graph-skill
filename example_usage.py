from client import DeepResearchEvidenceSynthesisGraphClient

def main():
    client = DeepResearchEvidenceSynthesisGraphClient()
    res = client.synthesize_research_graph('Quantum Computing in Drug Discovery')
    print('Deep Research Evidence Graph: ' + res['research_graph_id'] + ' (' + res['synthesized_report_title'] + ')')
    print('Evidence Nodes: ' + str(res['evidence_nodes_count']) + ' | Top Claim: ' + res['cross_citation_graph'][0]['claim'])
    print('Report URL: ' + res['executive_summary_markdown_url'])

if __name__ == '__main__':
    main()
