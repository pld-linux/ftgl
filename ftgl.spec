%define	_rc	rc5
Summary:	OpenGL frontend to freetype2
Summary(pl.UTF-8):	Nakładka OpenGL na freetype2 - łatwy dostęp do fontów z poziomu OpenGL
Name:		ftgl
Version:	2.1.3
Release:	0.%{_rc}.1
Epoch:		0
License:	LGPL
Group:		X11/Libraries
# original URL (dead ATM): http://opengl.geek.nz/ftgl/%{name}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/ftgl/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	c7879018cde844059495b3029b0b6503
#Patch0:		%{name}-Makefiles.patch
URL:		http://homepages.paradise.net.nz/henryj/code/#FTGL
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	ghostscript
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTGL is a free, open source library to enable developers to use
arbitrary fonts in their OpenGL (http://www.opengl.org/) applications.
Unlike other OpenGL font libraries FTGL uses standard font file formats
so doesn't need a preprocessing step to convert the high quality font
data into a lesser quality, proprietary format. FTGL uses the Freetype
(http://www.freetype.org/) font library to open and 'decode' the
fonts. It then takes that output and stores it in a format most
efficient for OpenGL rendering.

%description -l pl.UTF-8
FTPGL to wolnodostępna biblioteka z otwartymi źródłami umożliwiająca
programistom używanie dowolnych fontów w aplikacjach OpenGL
(http://www.opengl.org/). W przeciwieństwie do innych bibliotek OpenGL
FTGL używa standardowych formatów plików z fontami, dzięki czemu nie
jest wymagany żaden preprocessing, aby przetworzyć dane fontu wysokiej
jakości na własnościowy format niższej jakości. FTGL do wczytywania i
dekodowania fontów używa biblioteki obsługi fontów Freetype
(http://www.freetype.org/), następnie przejmuje wyjście i przechowuje
je w formacie najbardziej wydajnym przy renderingu OpenGL.

%package devel
Summary:	OpenGL frontend to freetype2 - development files
Summary(pl.UTF-8):	Nakładka OpenGL na freetype2 - pliki dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	freetype-devel >= 2.0.9
Requires:	libstdc++-devel

%description devel
OpenGL frontend to freetype2 - development files.

%description devel -l pl.UTF-8
Nakładka OpenGL na freetype2 - pliki dla programistów.

%package static
Summary:	Static FTGL library
Summary(pl.UTF-8):	Statyczna biblioteka FTGL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FTGL library.

%description static -l pl.UTF-8
Statyczna biblioteka FTGL.

%prep
%setup -q -n %{name}-%{version}~%{_rc}
#%%patch0 -p1
%{__sed} -i 's/\$(ECHO)/echo/' Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README docs/{*.dox,*.txt}
%attr(755,root,root) %{_libdir}/libftgl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/html
%attr(755,root,root) %{_libdir}/libftgl.so
%{_libdir}/libftgl.la
%{_includedir}/FTGL
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libftgl.a
