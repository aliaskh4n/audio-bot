from moviepy.editor import AudioFileClip

def convert_webm_audio_to_mp3(input_file, output_file):
    try:
        audio_clip = AudioFileClip(input_file)
        audio_clip.write_audiofile(output_file, codec='mp3')
        audio_clip.close()
    except Exception as e:
        print(f'Ошибка при конвертации аудио: {e}')