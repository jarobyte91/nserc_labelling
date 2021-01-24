from engine import app, db
from engine.models import UnlabelledExample, LabelledExample

@app.shell_context_processor
def make_shell_context():
    return {"db": db, 
            "UnlabelledExample": UnlabelledExample, 
            "LabelledExample": LabelledExample}
