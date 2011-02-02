Summary:	OpenGL frontend to freetype2
Summary(pl.UTF-8):	Nakładka OpenGL na freetype2 - łatwy dostęp do fontów z poziomu OpenGL
Name:		ftgl
Version:	2.1.3
Release:	0.rc5.1
Epoch:		0
License:	MIT
Group:		Libraries
# original URL (dead ATM): http://opengl.geek.nz/ftgl/%{name}-%{version}.tar.gz
Source0:	http://downloads.sourceforge.net/ftgl/%{name}-%{version}-rc5.tar.gz
# Source0-md5:	fcf4d0567b7de9875d4e99a9f7423633
URL:		http://homepages.paradise.net.nz/henryj/code/#FTGL
BuildRequires:	OpenGL-GLU-devel >= 1.2
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1.6
BuildRequires:	doxygen
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	texlive-pdftex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTGL is a free, open source library to enable developers to use
arbitrary fonts in their OpenGL (http://www.opengl.org/) applications.
Unlike other OpenGL font libraries FTGL uses standard font file
formats so doesn't need a preprocessing step to convert the high
quality font data into a lesser quality, proprietary format. FTGL uses
the Freetype (http://www.freetype.org/) font library to open and
'decode' the fonts. It then takes that output and stores it in a
format most efficient for OpenGL rendering.

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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel >= 1.2
Requires:	freetype-devel >= 2.0.9
Requires:	libstdc++-devel

%description devel
OpenGL frontend to freetype2 - development files.

%description devel -l pl.UTF-8
Nakładka OpenGL na freetype2 - pliki dla programistów.

%package static
Summary:	Static FTGL library
Summary(pl.UTF-8):	Statyczna biblioteka FTGL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FTGL library.

%description static -l pl.UTF-8
Statyczna biblioteka FTGL.

%prep
%setup -q -n %{name}-%{version}~rc5

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_path_LATEX=no \
	--enable-shared
%{__make} \
	ECHO=/bin/echo

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	ECHO=/bin/echo

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_libdir}/libftgl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libftgl.so.2

%files devel
%defattr(644,root,root,755)
%doc docs/html
%attr(755,root,root) %{_libdir}/libftgl.so
%{_libdir}/libftgl.la
%{_includedir}/FTGL
%{_pkgconfigdir}/ftgl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libftgl.a
