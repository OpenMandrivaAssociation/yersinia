Summary:	Network pen-testing tool
Name:		yersinia
Version:	0.7.2
Release:	%mkrel 0.20060323.3
License: 	GPL
Group: 		System/Servers
Source:		http://www.yersinia.net/download/%{name}-snapshot.tgz
URL: 		http://www.yersinia.net
BuildRequires:	gtk2-devel
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Yersinia is a network tool designed to take advantage of some weakeness in
different network protocols. It pretends to be a solid framework for analyzing
and testing the deployed networks and systems.

Currently, only attacks for the following network protocols are implemented:
* Spanning Tree Protocol (STP).
* Cisco Discovery Protocol (CDP).
* Dynamic Trunking Protocol (DTP).
* Dynamic Host Configuration Protocol (DHCP).
* Hot Standby Router Protocol (HSRP).
* 802.1q.
* Inter-Switch Link Protocol (ISL).
* VLAN Trunking Protocol (VTP).

%prep

%setup -q -n %{name}

%build
make distclean
rm -f configure
sh ./autogen.sh

%configure2_5x \
    --with-pcap-includes=%{_includedir}/pcap

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog FAQ INSTALL README THANKS TODO
%{_bindir}/*
%{_mandir}/man8/*


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.7.2-0.20060323.3mdv2011.0
+ Revision: 664861
- mass rebuild

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-0.20060323.2mdv2010.0
+ Revision: 382744
- rebuilt against libnet 1.1.3

* Thu Oct 30 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-0.20060323.1mdv2009.1
+ Revision: 298729
- use the "latest" snapshot

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-5mdv2009.1
+ Revision: 298633
- fix build
- rebuilt against libpcap-1.0.0

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-4mdv2009.0
+ Revision: 262940
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-3mdv2009.0
+ Revision: 262797
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.7.1-1mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-1mdv2008.0
+ Revision: 56114
- update to new version 0.7.1
- import yersinia


* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-3mdv2007.0
- buildrequires gtk2-devel

* Fri Jun 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-2mdv2007.0
- buildrequires pkgconfig

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2007.0
- new version

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-3mdk
- rebuilt against libnet1.1.2

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.6-2mdk
- Fix BuildRequires

* Tue Sep 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.6-1mdk
- first mdk release
