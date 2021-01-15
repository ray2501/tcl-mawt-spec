#
# spec file for package tcl-mawt
#

%define packagename mawt

Name:           tcl-mawt
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  tcl-devel >= 8.6
BuildRequires:  tk-devel >= 8.6
BuildRequires:  swig
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  libswscale-devel
Requires:       tcl >= 8.6
Requires:       tk >= 8.6
Requires:       ffmpeg
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Version:        0.4.0
Release:        0
Summary:        Movie Automation With Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://www.mawt.tcl3d.org/
Source0:        %{packagename}-%{version}.tar.gz
Patch0:         CMakeLists.patch
Patch1:         CMakeModules.patch

%description
MAWT is a Tcl package based on FFmpeg.
It provides high level procedures for movie automation with Tcl.

%prep
%setup -q -n %{packagename}-%{version}
%patch0
%patch1

%build
cmake CMakeLists.txt
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}/%{packagename}%{version}

