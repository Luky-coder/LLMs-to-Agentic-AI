from agents.orchestrator.orchestrator import Orchestrator
from agents.calendar.calendar_tool import CalendarTool
from agents.static_post.post_tool import PostTool
from agents.RAG.rag_tool import RAGTool
from db.saver import PublicationSaver
from agents.publisher.publisher_tool import Publisher

def run_calendar_tool(args):
    cal = CalendarTool()
    return cal.run(args)

def run_static_post_tool(args, image):
    args["image"] = image
    post_tool = PostTool()
    return post_tool.run(args)

def run_pipeline(prompt: str, image: str):
    
    saver = PublicationSaver()
    publisher = Publisher()

    rag_tool = RAGTool()
    aug_prompt = rag_tool.run(prompt)
    
    orchestrator = Orchestrator()
    plan = orchestrator.plan(aug_prompt)

    edito_cal = []
    publications = []


    for step in plan:
        tool_name = step["tool"]
        args = step["args"]

        if tool_name == "calendar":
            edito_cal = run_calendar_tool(args)

        elif tool_name == "static_post":
            post = run_static_post_tool(args, image)
            publications.append(post)

    for post in publications:
        post_id = post.get("id_publication")
        publication_date = next(
            (entry["date"] for entry in edito_cal if entry["id_publication"] == post_id), 
            None
        )
        
        if publication_date:
            post["publication_date"] = publication_date
        print("POST", post)
        saver.save_publication(post)
        print("SAVED")
        publisher.run(post)
    
    saver.close()
    
    return 0