# MK-Twitter-User-Info
 This program provides a simple and interactive way to retrieve and view Twitter user details in a graphical interface.
 
 python_requires='>=3.8'

 ![1](https://github.com/user-attachments/assets/782ebdbf-273f-4d72-be39-26b4ec0531ca)

![2](https://github.com/user-attachments/assets/e89d43dd-0601-419e-8a8a-858a4a24c6bc)
 
### Install:
pip install -r requirements.txt

### Key Capabilities of the Code:

1. **Fetch Twitter User Information**:
   - The code retrieves the following information for a specific Twitter user based on their **screen name** (the Twitter handle):
     - **User ID**: A unique identifier for the user on Twitter.
     - **Name**: The full name of the user (as shown on their profile).
     - **Screen Name**: The Twitter handle (e.g., `@username`).
     - **Location**: The location specified on the user's profile.
     - **Description**: The bio or profile description of the user.
     - **Followers Count**: The number of people following the user.
     - **Following Count**: The number of people the user is following.
     - **Account Creation Date**: The date the account was created.

2. **Asynchronous Data Fetching**:
   - The code uses asynchronous functions (`asyncio`) and threading to **fetch the data from Twitter without freezing the GUI**. This means the user interface remains responsive while the data is being retrieved from Twitter.
   
3. **Supports Arabic Text**:
   - The program can handle and display Arabic text correctly if the user’s profile contains it. This is especially useful for users who have bio information or names written in Arabic.

### What This Code Can Do:
- **Fetch Public Twitter User Data**: Given a valid Twitter screen name, the program will fetch and display detailed information about that user.
- **Real-Time Progress Feedback**: The code uses a progress bar to show the user that the program is working, which improves the user experience by indicating that data is being retrieved in the background.
- **Arabic Text Rendering**: If the user's profile contains Arabic text (for example, in their bio), it will display correctly in the interface.

### Limitations:
- **Limited to Public Information**: The program can only retrieve publicly available information about a Twitter user. It cannot fetch private or protected data.
- **Requires Internet Access**: Since the program fetches data from Twitter's API, it requires an active internet connection.
- **Error Messages in GUI**: While errors are handled gracefully, there’s no advanced error reporting system (e.g., log files), so any issue is simply displayed as a message in the memo box.

### Conclusion:
This code provides a simple, efficient way to retrieve public information from Twitter about a user through a graphical interface. It handles multiple pieces of data (e.g., bio, followers count, etc.) and displays them in a user-friendly manner, with basic support for non-English text like Arabic.

Please use this application responsibly and ethically, in accordance with Twitter’s terms of service and applicable laws. The author of this software bears no responsibility for any misuse or illegal activities conducted through this application.

By using this application, you agree that:

You will not use it for harmful or malicious purposes.
You will not violate any privacy rights or engage in unauthorized data collection.
You are solely responsible for how you choose to use this application.
The author is not liable for any actions or consequences resulting from improper use of the software.

### Special Thanks
This software uses the Twikit library for accessing the Twitter API Scraper. Special thanks to the Twikit developer for providing this excellent tool. You can find more about the project here: https://github.com/d60/twikit.
