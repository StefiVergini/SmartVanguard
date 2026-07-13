from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.ai import get_embedding, chat_with_context
from app.models.document import Document
from app.api.deps import get_db, get_current_user
from app.utils.prompts import get_prompt

router = APIRouter()

@router.post("/chat")
def chat(query: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    embedding = get_embedding(query)

    docs = (
    db.query(Document)
    .filter(Document.company_id == user.company_id)
    .order_by(Document.embedding.cosine_distance(embedding))
    .limit(5)
    .all()
    )

    context = "\n".join([d.content for d in docs])

    prompt = get_prompt(user.company_id, query, context, db)

    answer = chat_with_context(prompt)

    return {"answer": answer} 
