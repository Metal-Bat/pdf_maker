from fastapi import APIRouter, status, Response
from app.utils.tools import open_file_from_assets
from app.utils.pdf_generator import PdfGenerator
from app.schema.sample import Ticket
import asyncio

router = APIRouter(prefix="/sample", tags=["sample"])


@router.post("/ticket")
async def ticket(valid_data: Ticket) -> Response:
    """create sample ticket for data

    Args:
        valid_data (Ticket): name and gender in practical

    Returns:
        FileResponse: contains pdf file and request data
    """
    main_html_data = asyncio.create_task(open_file_from_assets("templates/sample/ticket/index.html", **valid_data.__dict__))
    data: object = PdfGenerator(
        main_html=await main_html_data,
        css="templates/sample/ticket/main.css",
        base_url="templates/sample/ticket/",
    )
    data = await data.render_pdf()
    return Response(content=data, media_type="application/pdf", status_code=status.HTTP_200_OK)
