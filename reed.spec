Summary:	An autoscrolling pager for UNIX systems
Summary(pl.UTF-8):	Przewijający się automatycznie program stronicujący dla systemów UNIX
Name:		reed
Version:	5.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.sacredchao.net/software/reed/%{name}-%{version}.tar.gz
# Source0-md5:	22c8d80dd6a81ecc6ef60662f2d1840c
Patch0:		%{name}-makefile.patch
URL:		http://www.sacredchao.net/software/reed/
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An autoscrolling pager for UNIX systems.

%description -l pl.UTF-8
Przewijający się automatycznie program stronicujący dla systemów UNIX.

%prep
%setup  -q
%patch -P0 -p1

%build
sed -e "s|curses\.h|ncurses\/curses.h|" cfg.data > .tmp
mv -f .tmp cfg.data
./configures \
	--libdir=%{_libdir}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/reed}

install reed breed wrap $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/reed
%{_mandir}/man*/*
