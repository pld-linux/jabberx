Summary:	Console client for the Jabber instant-messaging IM
Name:		jabberx
Version:	0.0.2
Release:	1
Group:		Applications
License:	GPL
Source0:	http://files.jabberstudio.org/jabberx/%{name}-%{version}.tar.gz
URL:		http://jabberx.jabberstudio.org/
BuildRequires:	iksemel-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JabberX is a console-mode client for the Jabber instant-messaging IM
platform. With JabberX, you can send and receive messages, browse and use
Jabber services, participate in Jabber groupchats and search Jabber user
directories.

%prep
%setup -q

%build
export CPPFLAGS="-I/usr/include/ncurses"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
