Summary:	openGL font library
Summary(pl):	latwy dostep do fontow z poziomu openGL
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
BuildRequires:	doxygen
BuildRequires:	OpenGL-devel
BuildRequires:  freetype-devel
Requires:	OpenGL
Requires:	freetype
Provides:	libftgl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTGL is a free, open source library to enable developers to use arbitrary fonts in their OpenGL (www.opengl.org) applications.
 Unlike other OpenGL font libraries FTGL uses standard font file formats so doesn't need a preprocessing step to convert the high quality font data into a lesser quality, proprietary format.
  FTGL uses the Freetype (www.freetype.org) font library to open and 'decode' the fonts. It then takes that output and stores it in a format most efficient for OpenGL rendering. 
  
%description -l pl

%package devel
Summary:	FTGL, developers resource
Group:		X11/Libraries

%description devel
FTGL, developers resource

%prep
%setup -q -n FTGL
%patch0 -p1

%build
cd unix
./configure \
	--with-pic \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd unix
%{__make} install install_prefix=$RPM_BUILD_ROOT 
mv $RPM_BUILD_ROOT/usr/share/doc/ftgl $RPM_BUILD_ROOT/usr/share/doc/%{name}-devel-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files devel
%defattr(644,root,root,755)

#!FIXME
#%doc COPYING.txt  HISTORY.txt  README.txt license.txt

%attr(644,root,root) %{_includedir}/*
%attr(755,root,root) %{_libdir}/*
%attr(644,root,root) %{_datadir}/*

%changelog
