Name:       libnl
Summary:    Convenience library for kernel netlink sockets
Version:    3.2.9
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://www.infradead.org/~tgr/libnl/
Source0:    http://www.infradead.org/~tgr/libnl/files/libnl-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  flex
BuildRequires:  byacc
BuildRequires:  bison

%description
This package contains a convenience library to simplify
using the Linux kernel's netlink sockets interface for
network manipulation

%package devel
Summary:    Libraries and headers for using libnl
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains various headers for using libnl

%package cli
Summary:    Command line interface utils for libnl
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description cli
This package contains various libnl3 utils and additional
libraries on which they depend.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# Makefile junk in the docs. Error by rpmlint.
find doc/ -name 'Makefile*' -exec rm '{}' \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post cli -p /sbin/ldconfig

%postun cli -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libnl-3.so.*
%{_libdir}/libnl-genl-3.so.*
%{_libdir}/libnl-nf-3.so.*
%{_libdir}/libnl-route-3.so.*
%config(noreplace) %{_sysconfdir}/*

%files devel
%defattr(-,root,root,-)
%doc doc/*
%{_includedir}/libnl3/netlink/
%dir %{_includedir}/libnl3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files cli
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libnl-cli*.so.*
%{_libdir}/libnl/
%{_sbindir}/*
%{_mandir}/man8/*
