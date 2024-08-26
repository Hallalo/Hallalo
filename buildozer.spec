[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapplication

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myapp

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['\"](.*)['\"]

# (str) Application icon
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Presplash background color (for android & iOS)
#presplash.color = #FFFFFF

# (str) Path to a custom whitelist file
#custom.whitelist = %(source.dir)s/custom_whitelist.txt

# (list) Custom source folders
#custom.source.folders = %(source.dir)s/src

# (list) Custom source files
#custom.source.files = my_custom_file.py

# (str) Custom service.py file
#custom.service = %(source.dir)s/service/service.py

# (str) Path to a custom blacklist file
#custom.blacklist = %(source.dir)s/custom_blacklist.txt

# (list) Custom Java class or files
#custom.java.files = %(source.dir)s/src/MyClass.java

# (str) Path to a custom blacklist file
#custom.blacklist = %(source.dir)s/custom_blacklist.txt

# (list) Custom resource directories
#custom.res_dirs = %(source.dir)s/res

# (list) Custom resource files
#custom.res_files = %(source.dir)s/data/image.png

# (list) Python files to ignore
#python.ignore = myfile.py

# (str) Kivy version to use
#kivy.version = 2.0.0

# (bool) Copy the content of `source.dir` to `source.packing_dir` when packing
#source.packaging = False


# Android specific

# (bool) Enable Android support
android = True

# (str) Android package name
#android.package = %(package.domain)s.%(package.name)s

# (str) Android bootstrap to use
#android.bootstrap = sdl2

# (str) Android min api level
#android.minapi = 21

# (int) Android SDK API to use
#android.sdk = 28

# (str) Android NDK API to use
#android.ndk = 21

# (str) Android build tool to use
#android.build_tool = 28.0.3

# (str) NDK API level to use
#android.ndk_api = 21

# (str) Android package name
#android.package_name = %(package.domain)s.%(package.name)s

# (str) Android presplash of the application
#android.presplash.filename = %(source.dir)s/data/presplash.png

# (str) Android presplash background color
#android.presplash.color = #FFFFFF

# (list) Permissions
#android.permissions = INTERNET,ACCESS_FINE_LOCATION

# (bool) Copy LIBS directories to "assets/libs" to avoid conflicts
#android.add_libs = True

# (bool) Include sqlite3 in the application
#android.include_sqlite3 = False

# (list) Services to include
#android.services = NAME:ENTRYPOINT_TO_PY

# iOS specific

# (bool) Enable iOS support
#ios = False

# (str) Path to a custom entitlements file
#ios.entitlements = %(source.dir)s/entitlements.plist

# (str) Path to a custom xcode framework
#ios.frameworks = %(source.dir)s/frameworks/

# (list) Additional frameworks to link
#ios.link_frameworks = my_custom_framework.framework

# (bool) Use --copy instead of --symlink when linking frameworks
#ios.copy_frameworks = False

# (list) iOS specific link flags
#ios.link_flags = -lz

# (str) Path to a custom launchscreen file
#ios.launchscreen = %(source.dir)s/launchscreen.xib

# (str) Path to a custom plist file
#ios.custom.plist = %(source.dir)s/custom.plist


# Windows specific

# (bool) Enable Windows support
#windows = False

# OSX specific

# (bool) Enable OSX support
#osx = False

# others

# (str) Path to a custom blacklist file
#custom.blacklist = %(source.dir)s/custom_blacklist.txt

# (list) Custom resource directories
#custom.res_dirs = %(source.dir)s/res

# (list) Custom resource files
#custom.res_files = %(source.dir)s/data/image.png

# (list) Custom resource files to exclude (let empty to not exclude anything)
#custom.res_files_exclude = %(source.dir)s/data/image.png

# (list) Additional resources to include (for android)
#android.resource_inclusion = resources

# (bool) Include encodings in the build
#encodings.included = True
