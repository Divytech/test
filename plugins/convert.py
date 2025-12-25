import os
from pyrogram import Client, filters
from pyrogram.types import Message
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the File Converter Bot! Send me an image or text file to convert it to PDF.")

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text("Help:\nSend an image (JPG/PNG) to convert to PDF.\nSend a text file (.txt) to convert to PDF.")

@Client.on_message(filters.photo)
async def image_to_pdf(client, message: Message):
    status_msg = await message.reply_text("Downloading image...")
    file_path = await message.download()
    
    new_file_path = f"{os.path.splitext(file_path)[0]}.pdf"
    
    try:
        await status_msg.edit_text("Converting to PDF...")
        image = Image.open(file_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(new_file_path, "PDF", resolution=100.0)
        
        await status_msg.edit_text("Uploading PDF...")
        await message.reply_document(new_file_path)
        os.remove(new_file_path)
        os.remove(file_path)
        await status_msg.delete()
    except Exception as e:
        await status_msg.edit_text(f"Error: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)

@Client.on_message(filters.document)
async def doc_handler(client, message: Message):
    if message.document.mime_type == "text/plain" or message.document.file_name.endswith(".txt"):
        await text_to_pdf(client, message)
    else:
        await message.reply_text("File type not supported for conversion yet.")

async def text_to_pdf(client, message: Message):
    status_msg = await message.reply_text("Downloading text file...")
    file_path = await message.download()
    new_file_path = f"{os.path.splitext(file_path)[0]}.pdf"
    
    try:
        await status_msg.edit_text("Converting to PDF...")
        
        c = canvas.Canvas(new_file_path, pagesize=letter)
        width, height = letter
        text_object = c.beginText(40, height - 40)
        text_object.setFont("Helvetica", 10)
        
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for line in lines:
            # Simple text wrapping could be added here, but for now just write lines
            # Check if we need a new page
            if text_object.getY() < 40:
                c.drawText(text_object)
                c.showPage()
                text_object = c.beginText(40, height - 40)
                text_object.setFont("Helvetica", 10)
            
            text_object.textLine(line.strip())
            
        c.drawText(text_object)
        c.save()
        
        await status_msg.edit_text("Uploading PDF...")
        await message.reply_document(new_file_path)
        os.remove(new_file_path)
        os.remove(file_path)
        await status_msg.delete()
    except Exception as e:
        await status_msg.edit_text(f"Error: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)
