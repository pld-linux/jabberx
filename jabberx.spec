Summary:	Console client for the Jabber instant-messaging IM
Summary(pl):	Terminalowy klient komunikatora Jabber
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
platform. With JabberX, you can send and receive messages, browse and
use Jabber services, participate in Jabber groupchats and search
Jabber user directories.

%description -l pl
JabberX jest terminalowym klientem dla platformy komunikacyjnej
Jabber. Przy u¿yciu JabberX mo¿na wysy³aæ i odbieraæ komunikaty,
przegl±daæ i u¿ywaæ us³ug Jabbera, uczestniczyæ w rozmowach grupowych
oraz przeszukiwaæ katalogi u¿ytkowników Jabbera.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
