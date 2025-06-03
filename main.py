import argparse
from agent import ResearchAgent


def main():
    parser = argparse.ArgumentParser(description="Academic Research Assistant Agent")
    parser.add_argument("query", help="Research query, e.g., 'transformers in NLP'")
    parser.add_argument(
        "--limit", type=int, default=3, help="Number of papers to process"
    )
    args = parser.parse_args()

    agent = ResearchAgent(args.query, limit=args.limit)
    ppt_path = agent.run()
    print(f"Generated presentation: {ppt_path}")


if __name__ == "__main__":
    main()
