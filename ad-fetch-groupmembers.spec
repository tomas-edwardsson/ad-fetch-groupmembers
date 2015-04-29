Name:		ad-fetch-groupmembers
Version:	1.5
Release:	1%{?dist}
Summary:	Fetches groupmembers from Active Directory for use in httpd

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/tomas-edwardsson/ad-fetch-groupmembers
Source0:	%{name}-%{version}.tar.gz

Requires:	python-ldap
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch



%description
Fetches groupmebers from a Active Directory server and outputs require statements
needed for authentication.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -q


%build
true


%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
install -D -m 600 ad-fetch-groupmembers.cfg $RPM_BUILD_ROOT/%{_sysconfdir}/ad-fetch-groupmembers.cfg
install -D -m 755 ad-fetch-groupmembers $RPM_BUILD_ROOT/%{_bindir}/ad-fetch-groupmembers

%files
%doc README.md gpl-3.0.txt
%config(noreplace) %{_sysconfdir}/ad-fetch-groupmembers.cfg
%{_bindir}/ad-fetch-groupmembers



%changelog
* Thu Feb 28 2013 Tomas Edwardsson <tommi@tommi.org> 1.5-1
- Minor fix (tommi@tommi.org)

* Thu Feb 28 2013 Tomas Edwardsson <tommi@tommi.org> 1.4-1
- Added releasers configuration (tommi@tommi.org)
- Initialized to use tito. (tommi@tommi.org)

* Thu Feb 28 2013 HUT Build <midtolvuhopur@lsh.is> 1.3-1
- 

* Thu Feb 28 2013 Tomas Edwardsson
- new package built with tito

* Thu Feb 14 2013 Tomas Edwardsson <tommi@tommi.org> 1.0-1
Initial packaging

