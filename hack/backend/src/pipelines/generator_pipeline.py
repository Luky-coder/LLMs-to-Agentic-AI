from agents.orchestrator.orchestrator import Orchestrator
from agents.calendar.calendar_tool import CalendarTool
from agents.static_post.post_tool import PostTool
from agents.RAG.rag_tool import RAGTool
from db.saver import PublicationSaver

def run_calendar_tool(args):
    cal = CalendarTool()
    return cal.run(args)

def run_static_post_tool(args, image):
    args["image"] = image
    post_tool = PostTool()
    return post_tool.run(args)

def run_pipeline(prompt: str, image: str):
    
    saver = PublicationSaver()
    # Exécution de l'outil RAG pour obtenir un prompt augmenté
    rag_tool = RAGTool()
    aug_prompt = rag_tool.run(prompt)
    
    # Planification des étapes à suivre
    orchestrator = Orchestrator()
    plan = orchestrator.plan(aug_prompt)

    # Listes pour stocker les résultats
    edito_cal = []
    publications = []

    # Exécution des outils de manière synchrone
    print(plan)
    for step in plan:
        tool_name = step["tool"]
        args = step["args"]

        if tool_name == "calendar":
            # Exécute l'outil Calendar et récupère le résultat
            edito_cal = run_calendar_tool(args)

        elif tool_name == "static_post":
            # Exécute l'outil Static Post et récupère le résultat
            post = run_static_post_tool(args, image)
            publications.append(post)

    # Attribution des dates de publication en fonction de l'éditeur de calendrier
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
    
    
    
    saver.close()
    
    return 0