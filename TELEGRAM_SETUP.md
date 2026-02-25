# Telegram Bot Configuration
# To set up your Telegram bot for order notifications:

## 1. Create a Telegram Bot:
1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (looks like: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz)

## 2. Get Your Chat ID:
1. Start a conversation with your bot
2. Send any message to the bot
3. Visit: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
4. Look for "chat" -> "id" in the response - this is your chat ID

## 3. Configure the Bot:
Replace the placeholder values in backend/collection_app/views.py:

Find these lines:
```python
bot_token = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
chat_id = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')
```

Replace with:
```python
bot_token = 'YOUR_ACTUAL_BOT_TOKEN'
chat_id = 'YOUR_ACTUAL_CHAT_ID'
```

Or set environment variables:
- TELEGRAM_BOT_TOKEN=your_bot_token
- TELEGRAM_CHAT_ID=your_chat_id

## 4. Test the Integration:
1. Restart the Django backend server
2. Submit a test order through the website
3. You should receive a formatted message in Telegram

## Example Telegram Message Format:
🛍️ NEW ORDER RECEIVED 🛍️

📦 Product Details:
• Product: Traditional Red Habesha
• Price: $450
• Size: M

👤 Customer Information:
• Name: John Doe
• Phone: +1234567890
• Delivery Address: 123 Main St, City, Country

📝 Special Notes:
Please deliver after 5 PM

📅 Time: 2/19/2026, 8:45:30 AM
