#
# Conditional build:
%bcond_with	bootstrap	# exclude gij/libgij.so
#
# TODO:
#		- http://gcc.gnu.org/PR11203 (inline-asm)
#		- http://gcc.gnu.org/PR18648 (missed tree-optimization)
#		- http://gcc.gnu.org/PR18910 (ICE: regression)
#		- http://gcc.gnu.org/PR19030 (ICE: regression)
#		- disable internal zlib usage
#		- bconds
#		- translations from gcc.spec:HEAD
#
%define		_snap		20041212
#
Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(pl):	Kolekcja kompilator�w GNU: kompilator C i pliki wsp�dzielone
Name:		gcc
Epoch:		5
Version:	4.0.0
Release:	0.%{_snap}.0.2
License:	GPL
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
#Source0:	ftp://gcc.gnu.org/pub/gcc/prerelease-%{version}-%{_snap}/gcc-%{version}-%{_snap}.tar.bz2
Source0:	ftp://gcc.gnu.org/pub/gcc/snapshots/4.0-%{_snap}/%{name}-4.0-%{_snap}.tar.bz2
# Source0-md5:	2bd9691c5ede05b27ce1f89b165abaa1
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolocalefiles.patch
Patch2:		%{name}-nodebug.patch
Patch3:		%{name}-ada-link-new-libgnat.patch
Patch4:		%{name}-ada-link.patch
Patch5:		%{name}-pr18928.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils >= 2:2.15.94.0.1
BuildRequires:	bison
BuildRequires:	fileutils >= 4.0.41
BuildRequires:	flex
BuildRequires:	gcc(ada)
BuildRequires:	gcc-ada
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel >= 2.2.5-20
BuildRequires:	gmp-devel
BuildRequires:	libmpfr-devel
BuildRequires:	perl-devel
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
Requires:	binutils >= 2:2.15.94.0.1
Requires:	libgcc = %{epoch}:%{version}-%{release}
Provides:	cpp = %{epoch}:%{version}-%{release}
Provides:	gcc(ada)
Obsoletes:	cpp
Obsoletes:	egcs-cpp
Obsoletes:	gcc-cpp
Obsoletes:	gcc-ksi
Obsoletes:	gont
Conflicts:	glibc-devel < 2.2.5-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description -l pl
Kompilator, posiadaj�cy du�e mo�liwo�ci optymalizacyjne niezb�dne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

Ten pakiet zawiera kompilator C i pliki wsp�dzielone przez r�ne
cz�ci kolekcji kompilator�w GNU (GCC). �eby u�ywa� innego kompilatora
z GCC, trzeba zainstalowa� odpowiedni podpakiet.

%package -n libgcc
Summary:	Shared gcc library
Summary(pl):	Biblioteka gcc
Group:		Libraries
Obsoletes:	libgcc1

%description -n libgcc
Shared gcc library.

%description -n libgcc -l pl
Biblioteka dynamiczna gcc.

%package -n libmudflap
Summary:	GCC mudflap shared support library
Group:		Libraries

%description -n libmudflap
The libmudflap�libraries�are�used by GCC for instrumenting pointer and
array dereferencing operations.

%package -n libmudflap-devel
Summary:	Development files for GCC mudflap library
Group:		Development/Libraries
Requires:	libmudflap = %{epoch}:%{version}-%{release}

%description -n libmudflap-devel
The libmudflap�libraries�are�used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%package -n libmudflap-static
Summary:	Static GCC mudflap library
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-static
The libmudflap�libraries�are�used by GCC for instrumenting pointer and
array dereferencing operations. This package contains static
libraries.

%package ada
Summary:	Ada support for gcc
Summary(pl):	Obs�uga Ady do gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgnat = %{epoch}:%{version}-%{release}
Obsoletes:	gcc-gnat
Obsoletes:	gnat-devel

%description ada
This package adds experimental support for compiling Ada programs.

%description ada -l pl
Ten pakiet dodaje eksperymentalne wsparcie dla kompilacji program�w w
Adzie.

%package -n libgnat
Summary:	Ada standard libraries
Summary(pl):	Biblioteki standardowe dla Ady
Group:		Development/Libraries
Obsoletes:	gnat
Obsoletes:	libgnat1

%description -n libgnat
This package contains shared libraries needed to run programs written
in Ada.

%description -n libgnat -l pl
Ten pakiet zawiera biblioteki potrzebne do uruchamiania program�w
napisanych w Adzie.

%package -n libgnat-static
Summary:	Static Ada standard libraries
Summary(pl):	Statyczne biblioteki standardowe dla Ady
Group:		Development/Libraries
Obsoletes:	gnat-static

%description -n libgnat-static
This package contains static libraries for programs written in Ada.

%description -n libgnat-static -l pl
Ten pakiet zawiera biblioteki statyczne dla program�w napisanych w
Adzie.

%package c++
Summary:	C++ support for gcc
Summary(pl):	Obs�uga C++ dla gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++

%description c++
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%description c++ -l pl
Ten pakiet dodaje obs�ug� C++ do kompilatora gcc. Ma wsparcie dla
du�ej ilo�ci obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, kt�re s� w oddzielnym pakiecie.

%package -n libstdc++
Summary:	GNU C++ library
Summary(pl):	Biblioteki GNU C++
Group:		Libraries
Obsoletes:	libg++
Obsoletes:	libstdc++3

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++ -l pl
Pakiet ten zawiera biblioteki b�d�ce implementacj� standardowych
bibliotek C++. Znajduj� si� w nim biblioteki dynamiczne niezb�dne do
uruchomienia aplikacji napisanych w C++.

%package -n libstdc++-devel
Summary:	Header files and documentation for C++ development
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki standardowej C++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	libstdc++ = %{epoch}:%{version}-%{release}
Obsoletes:	libg++-devel
Obsoletes:	libstdc++3-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++-devel -l pl
Pakiet ten zawiera biblioteki b�d�ce implementacj� standardowych
bibliotek C++. Znajduj� si� w nim pliki nag��wkowe wykorzystywane przy
programowaniu w j�zyku C++ oraz dokumentacja biblioteki standardowej.

%package -n libstdc++-static
Summary:	Static C++ standard library
Summary(pl):	Statyczna biblioteka standardowa C++
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libstdc++-static
Static C++ standard library.

%description -n libstdc++-static -l pl
Statyczna biblioteka standardowa C++.

%package fortran
Summary:	Fortran 95 support for gcc
Summary(pl):	Obs�uga Fortranu 95 dla gcc
Group:		Development/Languages/Fortran
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Obsoletes:	egcs-g77
Obsoletes:	gcc-g77

%description fortran
This package adds support for compiling Fortran 95 programs with the
GNU compiler.

%description fortran -l pl
Ten pakiet dodaje obs�ug� Fortranu 95 do kompilatora gcc. Jest
potrzebny do kompilowania program�w pisanych w j�zyku Fortran 95.

%package -n libgfortran
Summary:	Fortran 95 Libraries
Summary(pl):	Biblioteki Fortranu 95
Group:		Development/Libraries
Obsoletes:	libg2c

%description -n libgfortran
Fortran 95 Libraries.

%description -n libgfortran -l pl
Biblioteki Fortranu 95.

%package -n libgfortran-static
Summary:	Static Fortran 95 Libraries
Summary(pl):	Statyczne Biblioteki Fortranu 95
Group:		Development/Libraries
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Obsoletes:	libg2c-static

%description -n libgfortran-static
Static Fortran 95 Libraries.

%description -n libgfortran-static -l pl
Statyczne biblioteki Fortranu 95.

%package java
Summary:	Java support for gcc
Summary(pl):	Obs�uga Javy dla gcc
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgcj = %{epoch}:%{version}-%{release}
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Requires:	java-shared
Provides:	gcj = %{epoch}:%{version}-%{release}

%description java
This package adds experimental support for compiling Java(tm) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%description java -l pl
Wsparcie dla kompilowania program�w Java(tm) zar�wno do bajt-kodu jak
i do natywnego kodu. Dodatkowo wymagany jest pakiet libgcj, aby mo�na
by�o przeprowadzi� kompilacj�.

%package -n libgcj
Summary:	Java Class Libraries
Summary(pl):	Biblioteki Klas Javy
Group:		Libraries
Requires:	zlib
Obsoletes:	libgcj3

%description -n libgcj
Java Class Libraries.

%description -n libgcj -l pl
Biblioteki Klas Javy.

%package -n libgcj-devel
Summary:	Development files for Java Class Libraries
Summary(pl):	Pliki nag��wkowe dla Bibliotek Klas Javy
Group:		Development/Libraries
Requires:	%{name}-java = %{epoch}:%{version}-%{release}
Requires:	libgcj = %{epoch}:%{version}-%{release}
Obsoletes:	libgcj3-devel

%description -n libgcj-devel
Development files for Java Class Libraries.

%description -n libgcj-devel -l pl
Pliki nag��wkowe dla Bibliotek Klas Javy.

%package -n libgcj-static
Summary:	Static Java Class Libraries
Summary(pl):	Statyczne Biblioteki Klas Javy
Group:		Development/Libraries
Requires:	libgcj-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}

%description -n libgcj-static
Static Java Class Libraries.

%description -n libgcj-static -l pl
Statyczne Biblioteki Klas Javy.

%package -n libffi
Summary:	Foreign Function Interface library
Summary(pl):	Biblioteka zewn�trznych wywo�a� funkcji
Group:		Libraries

%description -n libffi
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run
time.

%description -n libffi -l pl
Biblioteka libffi dostarcza przeno�nego, wysokopoziomowego
mi�dzymordzia do r�nych konwencji wywo�a� funkcji. Pozwala to
programi�cie wywo�ywa� dowolne funkcje podaj�c konwencj� wywo�ania w
czasie wykonania.

%package -n libffi-devel
Summary:	Development files for Foreign Function Interface library
Summary(pl):	Pliki nag��wkowe dla libffi
Group:		Development/Libraries
Requires:	libffi = %{epoch}:%{version}-%{release}

%description -n libffi-devel
Development files for Foreign Function Interface library.

%description -n libffi-devel -l pl
Pliki nag��wkowe dla libffi.

%package -n libffi-static
Summary:	Static Foreign Function Interface library
Summary(pl):	Statyczna biblioteka libffi
Group:		Development/Libraries
Requires:	libffi-devel = %{epoch}:%{version}-%{release}

%description -n libffi-static
Static Foreign Function Interface library.

%description -n libffi-static -l pl
Statyczna biblioteka libffi.

%package java-tools
Summary:	Shared java tools
Summary(pl):	Wsp�dzielone narz�dzia javy
Group:		Development/Languages/Java
Provides:	jar = %{epoch}:%{version}-%{release}
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	java-shared
Obsoletes:	jar

%description java-tools
This package contains tools that are common for every Java(tm)
implementation, such as rmic or jar.

%description java-tools -l pl
Pakiet ten zawiera narz�dzia wsp�lne dla ka�dej implementacji
Javy(tm), takie jak rmic czy jar.

%package objc
Summary:	Objective C support for gcc
Summary(pl):	Obs�uga obiektowego C dla kompilatora gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libobjc = %{epoch}:%{version}-%{release}
Obsoletes:	egcc-objc
Obsoletes:	egcs-objc

%description objc
This package adds Objective C support to the GNU Compiler Collection.
Objective C is a object oriented derivative of the C language, mainly
used on systems running NeXTSTEP. This package does not include the
standard objective C object library.

%description objc -l pl
Ten pakiet dodaje obs�ug� obiektowego C do kompilatora gcc. Obiektowe
C (objc) jest zorientowan� obiektowo pochodn� j�zyka C, u�ywan�
g��wnie w systemach u�ywaj�cych NeXTSTEP. W pakiecie nie ma
standardowej biblioteki objc (kt�ra znajduje si� w osobnym pakiecie).

%package -n libobjc
Summary:	Objective C Libraries
Summary(pl):	Biblioteki Obiektowego C
Group:		Libraries
Obsoletes:	libobjc1

%description -n libobjc
Objective C Libraries.

%description -n libobjc -l pl
Biblioteki Obiektowego C.

%package -n libobjc-static
Summary:	Static Objective C Libraries
Summary(pl):	Statyczne Biblioteki Obiektowego C
Group:		Development/Libraries
Requires:	libobjc = %{epoch}:%{version}-%{release}

%description -n libobjc-static
Static Objective C Libraries.

%description -n libobjc-static -l pl
Statyczne biblioteki Obiektowego C.

%prep
# prerelease
#setup -q -n gcc-%{version}-%{_snap}
# snapshot
%setup -q -n gcc-4.0-%{_snap}
# final
#setup -q -n gcc-%{version}

#patch0 -p1	NEEDS UPDATE
%patch1 -p1
%{!?debug:%patch2 -p1}
%patch3 -p1
%patch4 -p1
%patch5 -p1

# because we distribute modified version of gcc...
perl -pi -e 's/(version.*)";/$1 (PLD Linux)";/' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

mv ChangeLog ChangeLog.general

%build
cd gcc
%{__autoconf}
cd ..
cp -f /usr/share/automake/config.sub .

rm -rf obj-%{_target_platform}
install -d obj-%{_target_platform}
cd obj-%{_target_platform}

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-__cxa_atexit \
	--enable-languages="c,c++,f95,objc,ada,java" \
	--enable-c99 \
	--enable-long-long \
%ifarch amd64
	--disable-multilib \
%else
	--enable-multilib \
%endif
	--enable-nls \
	--with-gnu-as \
	--with-gnu-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
	--without-x \
	--enable-cmath \
	%{_target_platform}

cd ..

%{__make} -C obj-%{_target_platform} \
	profiledbootstrap \
	GCJFLAGS="%{rpmcflags}" \
	BOOT_CFLAGS="%{rpmcflags}" \
	STAGE1_CFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

cd obj-%{_target_platform}

%{__make} -j1 install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

%ifarch sparc64
ln -sf	$RPM_BUILD_ROOT%{_bindir}/sparc64-pld-linux-gcc \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc
%endif

ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

ln -sf gfortran $RPM_BUILD_ROOT%{_bindir}/g95
echo ".so gfortran.1" > $RPM_BUILD_ROOT%{_mandir}/man1/g95.1

# move ada shared libraries to proper place...
mv -f	$RPM_BUILD_ROOT%{_libdir}/gcc/*/*/adalib/*.so.1 \
	$RPM_BUILD_ROOT%{_libdir}
# check if symlink to be made is valid
test -f	$RPM_BUILD_ROOT%{_libdir}/libgnat-4.0.so.1
ln -sf	libgnat-4.0.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnat-4.0.so
ln -sf	libgnarl-4.0.so.1 $RPM_BUILD_ROOT%{_libdir}/libgnarl-4.0.so
ln -sf	libgnat-4.0.so $RPM_BUILD_ROOT%{_libdir}/libgnat.so
ln -sf	libgnarl-4.0.so $RPM_BUILD_ROOT%{_libdir}/libgnarl.so
ln -sf	%{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp

cd ..

install -d java-doc
cp -f	libjava/READ* java-doc
cp -f	fastjar/README java-doc/README.fastjar
cp -f	libffi/README java-doc/README.libffi
cp -f	libffi/LICENSE java-doc/LICENSE.libffi
cp -f	libobjc/README gcc/objc/README.libobjc

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc/*/%{version}
for f in libstdc++.la libsupc++.la libgcj.la;
do
	perl -pi -e 's@-L[^ ]*[acs.] @@g' $RPM_BUILD_ROOT%{_libdir}/$f
done
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in libstdc++.la libsupc++.la libgfortran.la libgfortranbegin.la \
	libgcj.la lib-org-w3c-dom.la lib-org-xml-sax.la libffi.la libobjc.la;
do
	perl -pi -e "s@^libdir='.*@libdir='/usr/%{_lib}'@" $RPM_BUILD_ROOT%{_libdir}/$f
done

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*/)
mkdir	$gccdir/tmp
# we have to save these however
mv -f	$gccdir/include/{gcj,libffi/ffitarget.h,objc,syslimits.h} \
	$gccdir/tmp
rm -rf	$gccdir/include
mv -f	$gccdir/tmp \
	$gccdir/include
cp -f	$gccdir/install-tools/include/*.h \
	$gccdir/include
# but we don't want anything more from install-tools
rm -rf	$gccdir/install-tools

%find_lang gcc
%find_lang libstdc\+\+

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post ada
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun ada
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post fortran
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun fortran
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post java
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun java
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	-p /sbin/ldconfig -n libgcc
%postun	-p /sbin/ldconfig -n libgcc
%post	-p /sbin/ldconfig -n libmudflap
%postun	-p /sbin/ldconfig -n libmudflap
%post	-p /sbin/ldconfig -n libgnat
%postun	-p /sbin/ldconfig -n libgnat
%post	-p /sbin/ldconfig -n libstdc++
%postun	-p /sbin/ldconfig -n libstdc++
%post	-p /sbin/ldconfig -n libgfortran
%postun	-p /sbin/ldconfig -n libgfortran
%post	-p /sbin/ldconfig -n libgcj
%postun	-p /sbin/ldconfig -n libgcj
%post	-p /sbin/ldconfig -n libffi
%postun	-p /sbin/ldconfig -n libffi
%post	-p /sbin/ldconfig -n libobjc
%postun	-p /sbin/ldconfig -n libobjc

%files -f gcc.lang
%defattr(644,root,root,755)
%doc ChangeLog.general MAINTAINERS bugs.html faq.html
%doc gcc/{ChangeLog,ONEWS,README.Portability}
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/*
%dir %{_libdir}/gcc/*/*
%dir %{_libdir}/gcc/*/*/include

%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gccbug
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_bindir}/cc
%attr(755,root,root) %{_bindir}/cpp

%{_mandir}/man1/cc.1*
%{_mandir}/man1/cpp.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*

%{_infodir}/cpp*
%{_infodir}/gcc*

%attr(755,root,root) /lib/cpp

%attr(755,root,root) %{_slibdir}/lib*.so
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/specs
%attr(644,root,root) %{_libdir}/gcc/*/*/crt*.o
%ifarch sparc64
%{_libdir}/gcc/*/*/*/libgcc.a
%{_libdir}/gcc/*/*/*/libgcc_eh.a
%attr(644,root,root) %{_libdir}/gcc/*/*/*/crt*.o
%endif
%ifarch ppc
%attr(644,root,root) %{_libdir}/gcc/*/*/ecrt*.o
%attr(644,root,root) %{_libdir}/gcc/*/*/ncrt*.o
%{_libdir}/gcc/*/*/nof
%dir %{_libdir}/nof
%endif
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2

%{_libdir}/gcc/*/*/include/*.h

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/lib*.so.*

%files -n libmudflap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmudflap*.so.*.*.*

%files -n libmudflap-devel
%defattr(644,root,root,755)
%{_includedir}/mf-runtime.h
%{_libdir}/libmudflap*.la
%attr(755,root,root) %{_libdir}/libmudflap*.so

%files -n libmudflap-static
%defattr(644,root,root,755)
%{_libdir}/libmudflap*.a

%files ada
%defattr(644,root,root,755)
%doc gcc/ada/ChangeLog
%attr(755,root,root) %{_bindir}/gnat*
%attr(755,root,root) %{_bindir}/gpr*
%attr(755,root,root) %{_libdir}/libgnarl*.so
%attr(755,root,root) %{_libdir}/libgnat*.so
%attr(755,root,root) %{_libdir}/gcc/*/*/gnat1
%{_libdir}/gcc/*/*/adainclude
%dir %{_libdir}/gcc/*/*/adalib
%{_libdir}/gcc/*/*/adalib/*.ali
%{_libdir}/gcc/*/*/adalib/g-trasym.o
%{_libdir}/gcc/*/*/adalib/libgccprefix.a
%ifarch %{ix86}
%{_libdir}/gcc/*/*/adalib/libgmem.a
%endif
%{_datadir}/gnat
%{_infodir}/gnat*

%files -n libgnat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnarl*.so.1
%attr(755,root,root) %{_libdir}/libgnat*.so.1

%files -n libgnat-static
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/adalib/libgnarl.a
%{_libdir}/gcc/*/*/adalib/libgnat.a

%files c++
%defattr(644,root,root,755)
%doc gcc/cp/{ChangeLog,NEWS}
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/*-c++
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1plus
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%{_mandir}/man1/g++.1*

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%doc libstdc++-v3/{ChangeLog,README}
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/docs/html
%dir %{_includedir}/c++
%{_includedir}/c++/%{version}
%exclude %{_includedir}/c++/%{version}/java
%exclude %{_includedir}/c++/%{version}/javax
%exclude %{_includedir}/c++/%{version}/gcj
%exclude %{_includedir}/c++/%{version}/gnu
%exclude %{_includedir}/c++/%{version}/*/bits/stdc++.h.gch
%{_libdir}/libstdc++.la
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a

%files fortran
%defattr(644,root,root,755)
%doc gcc/fortran/ChangeLog
%attr(755,root,root) %{_bindir}/g95
%attr(755,root,root) %{_bindir}/gfortran
%{_infodir}/gfortran*
%attr(755,root,root) %{_libdir}/gcc/*/*/f951
%{_libdir}/libgfortranbegin.a
%{_libdir}/libgfortranbegin.la
%{_libdir}/libgfortran.la
%attr(755,root,root) %{_libdir}/libgfortran.so
%{_mandir}/man1/g95.1*
%{_mandir}/man1/gfortran.1*

%files -n libgfortran
%defattr(644,root,root,755)
%doc libgfortran/{AUTHORS,README,ChangeLog}
%attr(755,root,root) %{_libdir}/libgfortran.so.*.*.*

%files -n libgfortran-static
%defattr(644,root,root,755)
%{_libdir}/libgfortran.a

%files java
%defattr(644,root,root,755)
%doc gcc/java/ChangeLog java-doc/*
%attr(755,root,root) %{_bindir}/gcj*
%{!?with_bootstrap:%attr(755,root,root) %{_bindir}/gij}
%attr(755,root,root) %{_bindir}/grepjar
%attr(755,root,root) %{_bindir}/jcf-dump
%attr(755,root,root) %{_bindir}/jv-*
%attr(755,root,root) %{_bindir}/*-gcj*
%attr(755,root,root) %{_libdir}/gcc/*/*/jc1
%attr(755,root,root) %{_libdir}/gcc/*/*/jvgenmain
%{_infodir}/gcj*
%{_mandir}/man1/gcj*
%{!?with_bootstrap:%{_mandir}/man1/gij*}
%{_mandir}/man1/grepjar*
%{_mandir}/man1/jcf-*
%{_mandir}/man1/jv-*

%files java-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/grmi*
%attr(755,root,root) %{_bindir}/fastjar
%{_mandir}/man1/grmi*
%{_mandir}/man1/fastjar*
%{_infodir}/fastjar*

%files -n libgcj
%defattr(644,root,root,755)
%doc libjava/{ChangeLog,LIBGCJ_LICENSE,NEWS,README,THANKS}
%attr(755,root,root) %{_bindir}/addr2name.awk
%attr(755,root,root) %{_libdir}/lib*cj*.so.*.*.*
%{!?with_bootstrap:%attr(755,root,root) %{_libdir}/libgij.so.*.*.*}
%attr(755,root,root) %{_libdir}/lib-org*.so.*.*.*
%{_libdir}/logging.properties

%files -n libgcj-devel
%defattr(644,root,root,755)
%{_includedir}/c++/%{version}/java
%{_includedir}/c++/%{version}/javax
%{_includedir}/c++/%{version}/gcj
%{_includedir}/c++/%{version}/gnu
%{_libdir}/gcc/*/*/include/gcj
%dir %{_libdir}/security
%{_libdir}/security/*
%dir %{_datadir}/java
%{_datadir}/java/libgcj*.jar
%{_libdir}/lib*cj.spec
%{_libdir}/lib*cj*.la
%attr(755,root,root) %{_libdir}/lib*cj*.so
%{!?with_bootstrap:%{_libdir}/libgij.la}
%{!?with_bootstrap:%attr(755,root,root) %{_libdir}/libgij.so}
%attr(755,root,root) %{_libdir}/lib-org-*.so
%{_libdir}/lib-org-*.la
%{_pkgconfigdir}/libgcj.pc

%files -n libgcj-static
%defattr(644,root,root,755)
%{_libdir}/lib*cj*.a
%{!?with_bootstrap:%{_libdir}/libgij.a}
%{_libdir}/lib-org-*.a

%files -n libffi
%defattr(644,root,root,755)
%doc libffi/{ChangeLog,ChangeLog.libgcj,LICENSE,README}
%attr(755,root,root) %{_libdir}/libffi.so.*.*.*

%files -n libffi-devel
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/include/ffitarget.h
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi.la
%{_includedir}/ffi.h

%files -n libffi-static
%defattr(644,root,root,755)
%{_libdir}/libffi.a

%files objc
%defattr(644,root,root,755)
%doc gcc/objc/README
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1obj
%attr(755,root,root) %{_libdir}/libobjc.so
%{_libdir}/libobjc.la
%{_libdir}/gcc/*/*/include/objc

%files -n libobjc
%defattr(644,root,root,755)
%doc libobjc/{ChangeLog,README*}
%attr(755,root,root) %{_libdir}/libobjc.so.*.*.*

%files -n libobjc-static
%defattr(644,root,root,755)
%{_libdir}/libobjc.a
