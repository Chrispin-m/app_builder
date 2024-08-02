# APK/MOBILE APP BUILDER FROM A WEBSITE 

**Author:** iChrispin  
**GitHub:** [Chrispin-m](https://github.com/Chrispin-m)

This project demonstrates how to build an Android APK from a JavaScript project using Cordova. This method is suitable for converting projects built with frameworks like Vue.js or React.js into mobile apps.

## Prerequisites

- Java Development Kit (JDK)
- Android Studio SDK
- Gradle
- Cordova
- Python 3.x
## Installation
(if on LInux)
1. Update your system:

   ```bash
   sudo apt update
   sudo apt upgrade
## Instructions

1. **Clone this repository or copy the script to your local machine.**

2. **Navigate to the directory containing the `build_app.py` script.**

3. **Run the script:**

    ```bash
    python app_builder.py
    ```

4. **Follow the prompts:**
    - Enter the path to your Vue.js project when asked.

5. **The script will:**
    - Check and install required Python packages.
    - Ensure Cordova is installed.
    - Create a Cordova project.
    - Add the Android platform to the Cordova project.
    - Build the Vue.js project.
    - Copy the built files to the Cordova `www` directory.
    - Build the Cordova project to generate the APK.

6. **After the script completes, the location of the generated APK file(s) will be printed:**
    - Debug APK: `platforms/android/app/build/outputs/apk/debug/app-debug.apk`
    - Release APK: `platforms/android/app/build/outputs/apk/release/app-release.apk`

## Notes

- Ensure you have a stable internet connection as the script will download required packages if they are not already installed.
- The generated APK files will be located in the `platforms/android/app/build/outputs/apk` directory within the Cordova project.

## License

This project is licensed under the MIT License.
