from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
import pandas as pd
from app.services.ai import get_embedding
from app.models.document import Document
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile, db: Session = Depends(get_db), user=Depends(get_current_user)):
    df = pd.read_csv(file.file)

    for _, row in df.iterrows():
        content = " | ".join([str(v) for v in row.values])
        embedding = get_embedding(content)

    doc = Document(
    content=content,
    embedding=embedding,
    company_id=user.company_id
    )

    db.add(doc)

    db.commit()
    return {"rows": len(df)} 
