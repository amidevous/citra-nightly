# Buildrequire using pkgconfig dependency
# for spec file work for Fedora CentOs Red Hat Entreprise and Open Suse
# + spec file conditional for use cmake 3 for old system including cmake 2 and cmake 3
Name:           citra-nightly
Version:        0.1920
Release:        1%{?dist}
Summary:        Citra is the world's most popular, open-source, 3DS emulator. 

License:        GPLv2
URL:            https://github.com/citra-emu/citra-nightly
Source0:        https://github.com/citra-emu/citra-nightly/releases/download/nightly-1920/citra-unified-source-20230607-238a574.tar.xz

# use cmake or cmake 3 package conditional
%if 0%{?fedora} <= 19 || 0%{?rhel} <= 8
BuildRequires:  cmake3
%else
BuildRequires:  cmake extra-cmake-modules
%endif
%if 0%{?fedora}
BuildRequires:  libcxx-devel
%endif
BuildRequires:  gcc gcc-c++ make automake autoconf rpm-build git
BuildRequires:  clang pkgconfig(dbus-1)
# SDL2-devel or libSDL2-devel dependency with pkgconfig
BuildRequires:  pkgconfig(sdl2)
# openssl devel package name for all system
BuildRequires:  openssl-devel
# qt6-qtbase-devel or qt6-base dependency with pkgconfig
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Platform)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
# qt6-qtbase-private-devel require online for fedora and rhel conditional
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  qt6-qtbase-private-devel
%endif
# qt6-qtmultimedia-devel or qt6-multimedia dependency with pkgconfig
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6SpatialAudio)
# portaudio devel package name for all system
BuildRequires:  portaudio-devel
# xorg-x11-server-devel or xorg-x11-util-devel dependency with pkgconfig
BuildRequires:  pkgconfig(xorg-server)
# libX11 and libXext devel package name for all system
BuildRequires:   libX11-devel libXext-devel
# jack-audio-connection-kit-devel or libjack-devel dependency with pkgconfig
BuildRequires:  pkgconfig(jack)
# pipewire devel package name for all system
BuildRequires:  pipewire-devel
# ffmpeg 4 dependency with conditional
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  ffmpeg-devel compat-ffmpeg4
%else
# ffmpeg 4 found for OpenSUSE Leap 15.3 and more fmmpeg 3 not recommend use
BuildRequires:  ffmpeg-4 ffmpeg-4-libavcodec-devel
%endif
# esound dependency with pkgconfig
BuildRequires:  pkgconfig(esound)
Requires:  pkgconfig(sdl2)
Requires:  openssl-devel
Requires:  pkgconfig(Qt6)
Requires:  pkgconfig(Qt6Concurrent)
Requires:  pkgconfig(Qt6Core)
Requires:  pkgconfig(Qt6DBus)
Requires:  pkgconfig(Qt6Gui)
Requires:  pkgconfig(Qt6Network)
Requires:  pkgconfig(Qt6OpenGL)
Requires:  pkgconfig(Qt6OpenGLWidgets)
Requires:  pkgconfig(Qt6Platform)
Requires:  pkgconfig(Qt6PrintSupport)
Requires:  pkgconfig(Qt6Sql)
Requires:  pkgconfig(Qt6Test)
Requires:  pkgconfig(Qt6Widgets)
Requires:  pkgconfig(Qt6Xml)
Requires:  pkgconfig(Qt6Multimedia)
Requires:  pkgconfig(Qt6MultimediaWidgets)
Requires:  pkgconfig(Qt6SpatialAudio)
Requires:  portaudio
Requires:  pkgconfig(xorg-server)
Requires:   libX11 libXext
Requires:  pkgconfig(jack)
Requires:  pipewire
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  ffmpeg compat-ffmpeg4
%else
# ffmpeg 4 found for OpenSUSE Leap 15.3 and more fmmpeg 3 not recommend use
BuildRequires:  ffmpeg-4
%endif
Requires:  pkgconfig(esound)

%description
Citra is the world's most popular, open-source, Nintendo 3DS emulator
It is written in C++ with portability in mind and builds are actively maintained for Windows, Linux, Android and macOS
The emulator is capable of running most commercial games at full speed, provided you meet the necessary hardware requirements
Citra has two main release channels: Nightly and Canary
The Nightly build is based on the master branch, and contains already reviewed and tested features
The Canary build is based on the master branch, but with additional features still under review. PRs tagged canary-merge are merged only into the Canary builds.


%prep
%autosetup -p1 -n citra-unified-source-20230607-238a574


%build
rm -rf externals/boost/ externals/nihstro/
git clone https://github.com/citra-emu/ext-boost.git externals/boost
git clone https://github.com/neobrain/nihstro.git externals/nihstro
rm -rf externals/soundtouch/ externals/catch2/
git clone https://codeberg.org/soundtouch/soundtouch.git externals/soundtouch
git clone https://github.com/catchorg/Catch2 externals/catch2
rm -rf externals/dynarmic/ externals/xbyak/
git clone https://github.com/merryhime/dynarmic.git externals/dynarmic
git clone https://github.com/herumi/xbyak.git externals/xbyak
rm -rf externals/fmt/ externals/enet/
git clone https://github.com/fmtlib/fmt.git externals/fmt
git clone https://github.com/lsalzman/enet.git externals/enet
rm -rf externals/inih/inih/ externals/libressl/
git clone https://github.com/benhoyt/inih.git externals/inih/inih
git clone https://github.com/citra-emu/ext-libressl-portable.git externals/libressl
rm -rf externals/libusb/libusb/ externals/cubeb/
git clone https://github.com/libusb/libusb.git externals/libusb/libusb
git clone https://github.com/mozilla/cubeb externals/cubeb
rm -rf  externals/discord-rpc/ externals/cpp-jwt/
git clone https://github.com/discord/discord-rpc.git externals/discord-rpc
git clone https://github.com/arun11299/cpp-jwt.git externals/cpp-jwt
rm -rf externals/teakra/ externals/lodepng/lodepng/
git clone https://github.com/wwylele/teakra.git externals/teakra
git clone https://github.com/lvandeve/lodepng.git externals/lodepng/lodepng
rm -rf externals/zstd/ externals/libyuv/
git clone https://github.com/facebook/zstd.git externals/zstd
git clone https://github.com/lemenkov/libyuv.git externals/libyuv
rm -rf externals/sdl2/SDL/ externals/cryptopp-cmake/
git clone https://github.com/libsdl-org/SDL externals/sdl2/SDL
git clone https://github.com/abdes/cryptopp-cmake.git externals/cryptopp-cmake
rm -rf externals/cryptopp/ externals/dds-ktx/
git clone https://github.com/weidai11/cryptopp.git externals/cryptopp
git clone https://github.com/septag/dds-ktx externals/dds-ktx
rm -rf externals/openal-soft/ externals/glslang/
git clone https://github.com/kcat/openal-soft externals/openal-soft
git clone https://github.com/KhronosGroup/glslang externals/glslang
rm -rf externals/vma/ externals/vulkan-headers/ externals/sirit/
git clone https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator externals/vma
git clone https://github.com/KhronosGroup/Vulkan-Headers externals/vulkan-headers
git clone https://github.com/yuzu-emu/sirit externals/sirit
mkdir -p rpmbuildcmake
pushd rpmbuildcmake
# use cmake or cmake 3 package conditional
%if 0%{?fedora} <= 19 || 0%{?rhel} <= 8
%cmake3 -DOPENSL_INCLUDE_DIR=%{_includedir}/openssl  -DOPENSL_ANDROID_INCLUDE_DIR=%{_libdir} -DOPENSL_LIBRARY=%{_libdir} -DCMAKE_INSTALL_PREFIX=/opt/citra-nightly ../
%cmake3_build
%else
%cmake -DOPENSL_INCLUDE_DIR=%{_includedir}/openssl  -DOPENSL_ANDROID_INCLUDE_DIR=%{_libdir} -DOPENSL_LIBRARY=%{_libdir} -DCMAKE_INSTALL_PREFIX=/opt/citra-nightly ../
%cmake_build
%endif
popd

%install
pushd rpmbuildcmake
# use cmake or cmake 3 package conditional
%if 0%{?fedora} <= 19 || 0%{?rhel} <= 8
%cmake3_install
%else
%cmake_install
%endif
popd


%files
%license license.txt
%doc README.md


%changelog
* Mon Jun 12 2023 amy devous <amidevous@gmail.com> 0.1920-1
- initial build
