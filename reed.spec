Summary:	An autoscrolling pager for UNIX systems
Summary(pl):	Skroluj±cy siê automatycznie pager dla systemów UNIX
Name:		reed
Version:	5.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.sacredchao.net/software/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
BuildRequires:	ncurses-devel
Requires:	perl
URL:		http://www.sacredchao.net/software/reed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An autoscrolling pager for UNIX systems.

%description -l pl
Skroluj±cy siê automatycznie pager dla systemów UNIX.

%prep
%setup  -q
%patch0 -p1

%build
sed -e "s|curses\.h|ncurses\/curses.h|" cfg.data > .tmp
mv -f .tmp cfg.data
./configures
%{__make} CC=%{__cc} CFLAGS="-I%{_includedir}/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/reed}

install reed breed wrap $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/reed
%{_mandir}/man*/*
