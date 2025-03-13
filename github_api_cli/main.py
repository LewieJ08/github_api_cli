import requests  # type: ignore
import os

def main():
    while True:
        username = input("GitHub-Activity> ")
        if username == "exit":
            break

        url = f"https://api.github.com/users/{username}/events"
        data = requests.get(url)

        if data.status_code == 200:
            data = data.json()

            for event in data:

                if event['type'] == 'IssueCommentEvent':
                    print(f"- {username} commented on issue {event['payload']['issue']['number']}")
                elif event['type'] == 'PushEvent':
                    print(f"- {username} pushed to {event['repo']['name']}")
                elif event['type'] == 'IssuesEvent':
                    print(f"- {username} created issue {event['payload']['issue']['number']}")
                elif event['type'] == 'WatchEvent':
                    print(f"- {username} starred {event['repo']['name']}")
                elif event['type'] == 'PullRequestEvent':
                    print(f"- {username} created pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'PullRequestReviewEvent':
                    print(f"- {username} reviewed pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'PullRequestReviewCommentEvent':
                    print(f"- {username} commented on pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'CreateEvent':
                    print(f"- {username} created {event['payload']['ref_type']} {event['payload']['ref']}")
                else:
                    print(f"- {username} {event['type']}")

        else:
            print("Error, request invalid or timed out")

if __name__ == "__main__":
    main()