Summary:	OpenGL frontend to freetype2
Summary(pl):	Nak�adka OpenGL na freetype2 - �atwy dost�p do font�w z poziomu OpenGL
Name:		ftgl
Version:	2.1.2
Release:	1
Epoch:		0
License:	LGPL
Group:		X11/Libraries
# original URL (dead ATM): http://opengl.geek.nz/ftgl/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.pl.debian.org/pub/debian/pool/main/f/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	3eabec9ad37371c4d139408c7ffd2429
Patch0:		%{name}-Makefiles.patch
URL:		http://homepages.paradise.net.nz/henryj/code/#FTGL
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
FTGL is a free, open source library to enable developers to use
arbitrary fonts in their OpenGL (http://www.opengl.org/) applications.
Unlike other OpenGL font libraries FTGL uses standard font file formats
so doesn't need a preprocessing step to convert the high quality font
data into a lesser quality, proprietary format. FTGL uses the Freetype
(http://www.freetype.org/) font library to open and 'decode' the
fonts. It then takes that output and stores it in a format most
efficient for OpenGL rendering.

%description -l pl
FTPGL to wolnodost�pna biblioteka z otwartymi �r�d�ami umo�liwiaj�ca
programistom u�ywanie dowolnych font�w w aplikacjach OpenGL
(http://www.opengl.org/). W przeciwie�stwie do innych bibliotek OpenGL
FTGL u�ywa standardowych format�w plik�w z fontami, dzi�ki czemu nie
jest wymagany �aden preprocessing, aby przetworzy� dane fontu wysokiej
jako�ci na w�asno�ciowy format ni�szej jako�ci. FTGL do wczytywania i
dekodowania font�w u�ywa biblioteki obs�ugi font�w Freetype
(http://www.freetype.org/), nast�pnie przejmuje wyj�cie i przechowuje
je w formacie najbardziej wydajnym przy renderingu OpenGL.

%package devel
Summary:	OpenGL frontend to freetype2 - development files
Summary(pl):	Nak�adka OpenGL na freetype2 - pliki dla programist�w
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	freetype-devel

%description devel
OpenGL frontend to freetype2 - development files.

%description devel -l pl
Nak�adka OpenGL na freetype2 - pliki dla programist�w.

%prep
%setup -q -n FTGL
%patch0 -p1

%build
cd unix
install /usr/share/automake/config.* .
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
