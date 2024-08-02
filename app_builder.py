import os
import subprocess
import shutil
import sys

def print_introduction():
    print("\033[92m" + "*" * 50 + "\033[0m")
    print("\033[96mWelcome to the Android APK Builder!\033[0m")
    print("\033[92m" + "*" * 50 + "\033[0m")
    print("\033[94mAuthor: iChrispin\033[0m")
    print("\033[94mGitHub: https://github.com/Chrispin-m\033[0m")
    print("\033[93mThis script will help you convert your js like Vue.js project into an Android APK using Cordova.\033[0m")
    print("\033[92m" + "*" * 50 + "\033[0m")

def check_and_install(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", package_name])
    except subprocess.CalledProcessError:
        print(f"\033[93m{package_name} not found. Installing...\033[0m")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, cwd=cwd, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        print("\033[91mAn error occurred. Exiting...\033[0m")
        print("\033[91mGIVE ME THE JOB FOR QUALITY WORK CONTACT ME VIA MY GITHUB PAGE ON https://github.com/Chrispin-m\033[0m")
        sys.exit(1)

def main():
    print_introduction()

    # Check and install required packages
    check_and_install("nodeenv")
    
    # Ensure Cordova is installed
    try:
        subprocess.run(["cordova", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("\033[93mCordova is not installed. Installing...\033[0m")
        run_command("npm install -g cordova")

    # Get user inputs
    vue_project_path = input("\033[94mEnter the path to your Vue.js project: \033[0m").strip()
    cordova_project_name = input("\033[94mEnter the desired App Name: \033[0m").strip()
    cordova_app_id =  input("\033[94mEnter the desired App Name eg com.yourcompany.appname: \033[0m").strip()

    # Create Cordova project
    run_command(f"cordova create {cordova_project_name}")
    
    cordova_project_path = os.path.join(os.getcwd(), cordova_project_name)
    
    # Change directory to the Cordova project
    os.chdir(cordova_project_path)
    
    # Add Android platform
    run_command("cordova platform add android")

    # Build Vue.js project
    os.chdir(vue_project_path)
    run_command("npm install")
    run_command("npm run build")

    # Copy built files to Cordova www directory
    www_path = os.path.join(cordova_project_path, "www")
    if os.path.exists(www_path):
        shutil.rmtree(www_path)
    shutil.copytree(os.path.join(vue_project_path, "dist"), www_path)

    # Build the Cordova project
    os.chdir(cordova_project_path)
    run_command("cordova build android")

    # Find and print the location of the APK file
    apk_debug_path = os.path.join(cordova_project_path, "platforms/android/app/build/outputs/apk/debug/app-debug.apk")
    apk_release_path = os.path.join(cordova_project_path, "platforms/android/app/build/outputs/apk/release/app-release.apk")
    
    if os.path.exists(apk_debug_path):
        print(f"\033[92mDebug APK created at: {apk_debug_path}\033[0m")
    if os.path.exists(apk_release_path):
        print(f"\033[92mRelease APK created at: {apk_release_path}\033[0m")

if __name__ == "__main__":
    main()
