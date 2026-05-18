#
# Conditional build:
%bcond_without	tests		# unit tests
#
Summary:	AWS C Compression library
Summary(pl.UTF-8):	Biblioteka AWS C Compression
Name:		aws-c-compression
Version:	0.3.2
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/awslabs/aws-c-compression/releases
Source0:	https://github.com/awslabs/aws-c-compression/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	43fe6220d50678e2cf3290641bc11b53
URL:		https://github.com/awslabs/aws-c-compression
BuildRequires:	aws-c-common-devel
BuildRequires:	cmake >= 3.9
BuildRequires:	gcc >= 5:3.2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a cross-platform C99 implementation of compression algorithms
such as gzip, and Huffman encoding/decoding. Currently only Huffman is
implemented.

%description -l pl.UTF-8
Ten moduł jest wieloplatformową implementacją C99 algorytmów
kompresji, takich jak kodowanie/dekodowanie gzip czy Huffmana. Obecnie
zaimplementowany jest tylko algorytm Huffmana.

%package devel
Summary:	Header files for AWS C Compression library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AWS C Compression
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aws-c-common-devel

%description devel
Header files for AWS C Compression library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AWS C Compression.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%{_libdir}/libaws-c-compression.so.1.0.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libaws-c-compression.so
%{_includedir}/aws/compression
%{_libdir}/cmake/aws-c-compression
