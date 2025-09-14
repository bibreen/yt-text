#!/usr/bin/env python3

import sys
import click
from .downloader import get_transcript_text_with_yt_dlp


@click.command()
@click.argument('youtube_id')
@click.option('--chrome', is_flag=True, help='Use cookies from Chrome browser')
def cli(youtube_id, chrome):
    """Download transcript for a YouTube video."""
    try:
        transcript = get_transcript_text_with_yt_dlp(youtube_id, chrome)

        if transcript:
            print(transcript)
        else:
            click.echo("No transcript available for this video", err=True)
            sys.exit(1)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    cli()