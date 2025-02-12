import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file) #dump(what to write,where to write)
    
def list_all_videos(videos):
    print('\n')
    print("*" * 100)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']},Duration:{video['time']}")

    print('\n')
    print("*" * 100)

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video duration: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter video number you want to update"))
    if 1<=index<=len(videos):
        name = input("Enter video name: ")
        time = input("Enter video duration: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid number selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number you want to delete"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid number selected")

def main():
    videos=load_data()
    while True:
        print("\n YouTube Manager | Choose an option: ")
        print("1. List all youtube videos: ")
        print("2. Add a youtube videos: ")
        print("3. Update a youtube videos: ")
        print("4. Delete a youtube videos: ")
        print("5. Exit Application: ")
        choice=input("Enter your choice: ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__=="__main__":
    main()


