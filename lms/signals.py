from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
import subprocess
import json
from datetime import timedelta
import tempfile
import os

@receiver(post_save, sender=Video)
def extract_video_duration(sender, instance, created, **kwargs):
    """Automatically extract video duration after video is uploaded"""
    
    # Only process if video_file exists and duration is not yet set
    if instance.video_file and not instance.duration:
        try:
            # Create temporary file to process video
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                # Read video file from S3
                instance.video_file.seek(0)
                for chunk in instance.video_file.chunks():
                    tmp_file.write(chunk)
                tmp_file_path = tmp_file.name
            
            # Use ffprobe to extract video metadata
            cmd = [
                'ffprobe',
                '-v', 'quiet',
                '-print_format', 'json',
                '-show_format',
                '-show_streams',
                tmp_file_path
            ]
            
            # Run ffprobe command
            result = subprocess.run(cmd, capture_output=True, text=True)
            data = json.loads(result.stdout)
            
            # Extract duration in seconds
            duration_seconds = float(data['format']['duration'])
            
            # Delete temporary file
            os.unlink(tmp_file_path)
            
            # Update duration in database (without triggering save again)
            Video.objects.filter(pk=instance.pk).update(
                duration=timedelta(seconds=duration_seconds)
            )
            
            print(f"✓ Duration extracted for '{instance.title}': {duration_seconds} seconds")
            
        except FileNotFoundError:
            print("❌ FFmpeg/FFprobe not installed. Install: sudo apt install ffmpeg")
        except Exception as e:
            print(f"❌ Error extracting duration for '{instance.title}': {e}")