Summary:	Data compression library providing in-memory LZMA compression and decompression
Summary(pl.UTF-8):	Biblioteka zapewniająca kompresję i dekompresję LZMA dla danych w pamięci
Name:		lzlib
Version:	1.11
Release:	1
# library license is (2-clause) BSD
# minilzip license is GPL v2, but it's not packaged
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/lzip/lzlib/%{name}-%{version}.tar.lz
# Source0-md5:	0c8b1dbb716d685af9c4460ecf245102
Patch0:		%{name}-info.patch
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lzlib is a data compression library providing in-memory LZMA
compression and decompression functions, including integrity checking
of the decompressed data. The compressed data format used by the
library is the lzip format. Lzlib is written in C.

%description -l pl.UTF-8
Lzlib to biblioteka kompresji danych zapewniająca funkcje do kompresji
i dekompresji LZMA w pamięci wraz z kontrolą integralności
dekompresowanych danych. Format skompresowanych danych używany przez
bibliotekę to format lzip. Biblioteka jest napisana w C.

%package devel
Summary:	Header file for lzlib library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki lzlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for lzlib library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki lzlib.

%package static
Summary:	Static lzlib library
Summary(pl.UTF-8):	Statyczna biblioteka lzlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lzlib library.

%description static -l pl.UTF-8
Statyczna biblioteka lzlib.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-shared
%{__make} all info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/liblz.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liblz.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblz.so
%{_includedir}/lzlib.h
%{_infodir}/lzlib.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblz.a
