%define		_modname	yaz
%define		_status		stable

Summary:	%{_modname} - a Z39.50 client for PHP
Summary(pl):	%{_modname} - klient Z39.50 dla PHP
Name:		php-pecl-%{_modname}
Version:	1.0.4
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	2ae4180bcfc00199c465815f89fc3b16
URL:		http://pecl.php.net/package/yaz/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	yaz-devel
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
Obsoletes:	php-yaz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension implements a Z39.50 client for PHP using the YAZ
toolkit.

Find more information at: http://www.indexdata.dk/phpyaz/
http://www.indexdata.dk/yaz/

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie implementuje klienta Z39.50 dla PHP za pomoc± narzêdzi
YAZ.

Wiêcej informacji mo¿na znale¼æ na stronach:
http://www.indexdata.dk/phpyaz/ http://www.indexdata.dk/yaz/

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
