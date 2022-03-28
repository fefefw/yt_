from ytop.pipline.steps.get_video_list import GetVideoList

from ytop.pipline.pipline import Pipeline

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        "channel_id": CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
