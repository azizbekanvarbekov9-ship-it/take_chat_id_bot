deploy:
	@echo "Deploying the bot..."
	sudo cp -r ./calback_data_click_bot.service /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl start calback_data_click_bot.service
	sudo systemctl enable calback_data_click_bot.service
	@echo "Bot deployed successfully."

restart:
	@echo "Restarting the bot..."
	sudo systemctl restart calback_data_click_bot.service

status:
	@echo "Checking the bot status..."
	sudo systemctl status calback_data_click_bot.service
