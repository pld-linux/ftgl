Summary:	OpenGL frontend for freetype2
Summary(pl):	£atwy dostep do fontow z poziomu OpenGL
Name:		ftgl
Version:	2.1.2
Release:	1
Epoch:		0
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.pl.debian.org/pub/debian/pool/main/f/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	3eabec9ad37371c4d139408c7ffd2429
Patch0:		%{name}-Makefiles.patch
URL:		http://homepages.paradise.net.nz/henryj/code/#FTGL
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	OpenGL-devel
BuildRequires:	glut-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
FTGL is a free, open source library to enable developers to use
arbitrary fonts in their OpenGL (www.opengl.org) applications. Unlike
other OpenGL font libraries FTGL uses standard font file formats so
doesn't need a preprocessing step to convert the high quality font
data into a lesser quality, proprietary format. FTGL uses the Freetype
(www.freetype.org) font library to open and 'decode' the fonts. It
then takes that output and stores it in a format most efficient for
OpenGL rendering.

%description -l pl

%package devel
Summary:	OpenGL frontend for freetype2
Group:		X11/Libraries
Requires:	freetype-devel
Requires:	OpenGL-devel
Requires:	glut-devel

%description devel
OpenGL frontend for freetype2

%prep
%setup -q -n FTGL
%patch0 -p1

%build
cd unix
install %{_datadir}/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}

%{makeinstall} -C unix

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING.txt HISTORY.txt README.txt $RPM_BUILD_ROOT%{_datadir}/doc/ftgl/*
%{_includedir}/FTGL
%{_libdir}/*.*
%{_pkgconfigdir}/*.pc
