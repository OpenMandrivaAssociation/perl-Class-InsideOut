%define upstream_name       Class-InsideOut
%define upstream_version 1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    A safe, simple inside-out object construction kit
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Config)
BuildRequires: perl(Exporter)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a simple, safe and streamlined toolkit for building inside-out objects.
Unlike most other inside-out object building modules already on CPAN, this
module aims for minimalism and robustness:

* Does not require derived classes to subclass it
* Uses no source filters, attributes or CHECK blocks
* Supports any underlying object type including black-box inheritance
* Does not leak memory on object destruction
* Overloading-safe
* Thread-safe for Perl 5.8.5 or better
* mod_perl compatible
* Makes no assumption about inheritance or initializer needs

It provides the minimal support necessary for creating safe inside-out objects
and generating flexible accessors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/Class


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 680822
- mass rebuild

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 421133
- update to 1.10

* Sat Aug 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 419636
- new perl version macro
- fix summary and description

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.09-3mdv2009.0
+ Revision: 255988
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2008.1
+ Revision: 152962
- update to new version 1.09
- update to new version 1.09

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.1
+ Revision: 106602
- import perl-Class-InsideOut


