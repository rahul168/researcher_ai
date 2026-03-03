from dotenv import load_dotenv
from deep_research_app import launch_app

load_dotenv(override=True)


if __name__ == "__main__":
    demo = launch_app()
    demo.launch(inbrowser=True)
