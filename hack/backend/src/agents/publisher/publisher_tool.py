import base64
import requests
from datetime import datetime
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

load_dotenv()


class Publisher:
    """
    A class responsible for uploading and publishing image posts to LinkedIn using LinkedIn's API.
    """
    def __init__(self):
        """
        Initializes the Publisher by loading required environment variables for LinkedIn API access.
        """
        self.ACCESS_TOKEN = os.getenv("LK_TOKEN")
        self.PERSON_URN = os.getenv("LK_URN")
        self.URL = os.getenv("LK_URL")

    def run(self, input_data) -> dict:

        """
        Processes a list of post dictionaries, uploads images to LinkedIn, and publishes them as posts.

        Each post in `input_data` must contain a base64-encoded image. The function:
        1. Registers the upload with LinkedIn.
        2. Uploads the image to LinkedIn using the returned URL.
        3. Creates a post using the uploaded image.

        Note:
            This method assumes a `CAPTION` attribute exists on `self`, but it's missing from __init__.
            Make sure to set `self.CAPTION` before calling this method.

        Args:
            input_data (list): A list of dictionaries, each containing at least a base64-encoded image string under the "image" key.

        Returns:
            dict: Not explicitly returned, but prints the LinkedIn post response status and message for each publication.
        """

        for postlk in input_data:
            headers = {"Authorization": f"Bearer {self.ACCESS_TOKEN}"}

            register_url = self.URL
            upload_data = {
                "registerUploadRequest": {
                    "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                    "owner": self.PERSON_URN,
                    "serviceRelationships": [
                        {
                            "relationshipType": "OWNER",
                            "identifier": "urn:li:userGeneratedContent",
                        }
                    ],
                }
            }

            register_response = requests.post(
                register_url,
                headers={**headers, "Content-Type": "application/json"},
                json=upload_data,
            )
            register_json = register_response.json()
            upload_url = register_json["value"]["uploadMechanism"][
                "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"
            ]["uploadUrl"]
            asset_urn = register_json["value"]["asset"]
            image = postlk["image"]
            image_bytes = base64.b64decode(image, validate=True)
            upload_image = requests.put(upload_url, headers=headers, data=image_bytes)


            post_url = "https://api.linkedin.com/v2/ugcPosts"

            post_data = {
                "author": self.PERSON_URN,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": self.CAPTION},
                        "shareMediaCategory": "IMAGE",
                        "media": [
                            {
                                "status": "READY",
                                "description": {
                                    "text": "Image générée automatiquement"
                                },
                                "media": asset_urn,
                                "title": {"text": "Post auto"},
                            }
                        ],
                    }
                },
                "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
            }

            post_response = requests.post(
                post_url,
                headers={
                    "Authorization": f"Bearer {self.ACCESS_TOKEN}",
                    "X-Restli-Protocol-Version": "2.0.0",
                    "Content-Type": "application/json",
                },
                json=post_data,
            )

            print("Post status:", post_response.status_code)
            print("Response:", post_response.json())
