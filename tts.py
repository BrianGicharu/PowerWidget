from gtts import gTTS


lan = 'en'
shutdown_text = "Shutting down the computer"
restart_text = "Restarting the computer"
hibernate_text = "Hibernating the computer"
log_out_text = "Logging out the active user"
op_text = "Operation cancelled"

shutdown_audio = gTTS(text=shutdown_text, lang=lan, slow=False)
shutdown_audio.save("C:\\Users\\Brian\\IdeaProjects\\PowerWidget\\shutdown_text.wav")


restart_audio = gTTS(text=restart_text, lang=lan, slow=False)
restart_audio.save("C:\\Users\\Brian\\IdeaProjects\\PowerWidget\\restart_text.wav")

hibernate_audio = gTTS(text=hibernate_text, lang=lan, slow=False)
hibernate_audio.save("C:\\Users\\Brian\\IdeaProjects\\PowerWidget\\hibernate_text.wav")

log_out_audio = gTTS(text=log_out_text, lang=lan, slow=False)
log_out_audio.save("C:\\Users\\Brian\\IdeaProjects\\PowerWidget\\logout_text.wav")

op_audio = gTTS(text=op_text, lang=lan, slow=True)
op_audio.save("C:\\Users\\Brian\\IdeaProjects\\PowerWidget\\op_text.wav")
