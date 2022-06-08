from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

from lib.tg_stream import call_py


async def pstream(chat_id, file, audio=None):
    if audio:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(
                file,
                "./etc/banner.png",
                video_parameters=HighQualityAudio(),
            ),
            stream_type=StreamType().local_stream,
        )
    else:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(
                file,
                HighQualityAudio(),
                ),
            stream_type=StreamType().local_stream,
        )


async def pstream_audio(chat_id, file, thumb):
    await call_py.join_group_call(
        chat_id,
        AudioPiped(
            file,
            thumb,
            HighQualityAudio(),
        ),
        stream_type=StreamType().local_stream,
    )
