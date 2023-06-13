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
NoSource:       0

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



%build
cd %{_builddir}
rm -rf %{_builddir}/citra-unified-source-20230607-238a574 %{_builddir}/citra-nightly
git clone --branch nightly-1920 --recursive https://github.com/citra-emu/citra-nightly.git
mkdir -p %{_builddir}/citra-nightly/build
cd %{_builddir}/citra-nightly/build
# use cmake or cmake 3 package conditional
%if 0%{?fedora} <= 19 || 0%{?rhel} <= 8
cmake3 -DOPENSL_INCLUDE_DIR=%{_includedir}/openssl  -DOPENSL_ANDROID_INCLUDE_DIR=%{_libdir} -DOPENSL_LIBRARY=%{_libdir} -DCMAKE_INSTALL_PREFIX=/opt/citra-nightly ../
%cmake3_build
%else
cmake -DOPENSL_INCLUDE_DIR=%{_includedir}/openssl  -DOPENSL_ANDROID_INCLUDE_DIR=%{_libdir} -DOPENSL_LIBRARY=%{_libdir} -DCMAKE_INSTALL_PREFIX=/opt/citra-nightly ../
%cmake_build
%endif

%install
cd %{_builddir}/citra-nightly/build
# use cmake or cmake 3 package conditional
%if 0%{?fedora} <= 19 || 0%{?rhel} <= 8
%cmake3_install
%else
%cmake_install
%endif
cd %{_builddir}
rm -rf %{_builddir}/citra-unified-source-20230607-238a574 %{_builddir}/citra-nightly


%files
%license license.txt
%doc README.md


%changelog
* Mon Jun 12 2023 amy devous <amidevous@gmail.com> 0.1920-1
- initial build
