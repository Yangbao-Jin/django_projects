import * as React from "react";

export default function MyComponent() {
  return (
    <div className="bg-white flex flex-col max-md:max-w-full">
      <div className="flex max-w-full w-[1200px] flex-col self-center px-5">
        <div className="bg-white flex flex-col self-stretch pb-3.5 max-md:max-w-full">
          <div className="bg-red-600 flex flex-col self-stretch px-5 py-6 max-md:max-w-full">
            <div className="text-black text-base max-w-[531px] self-center ml-px mt-px -mb-0.5 max-md:max-w-full max-md:mb-2.5">
              Registration is open for the 2023-24 Season! It will be great
              one!!
            </div>
          </div>
          <div className="bg-white flex min-h-[56px] flex-col self-stretch max-md:max-w-full" />
          <div className="max-w-full w-[938px] ml-16 mt-6 max-md:ml-2.5">
            <div className="gap-5 flex max-md:flex-col max-md:items-stretch max-md:gap-0">
              <div className="flex flex-col items-stretch leading-[normal] w-[58%] max-md:w-full">
                <img
                  loading="lazy"
                  srcSet="https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=100 100w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=200 200w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=400 400w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=800 800w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=1200 1200w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=1600 1600w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?&width=2000 2000w, https://cdn.builder.io/api/v1/image/assets/TEMP/e326ffb3-8d97-4cd3-bf34-58143cde5988?"
                  className="aspect-[1.52] object-contain object-center w-full max-md:max-w-full max-md:mt-9"
                />
              </div>
              <div className="flex flex-col items-stretch leading-[normal] w-[42%] ml-5 max-md:w-full">
                <div className="flex flex-col mt-3.5 max-md:mt-12">
                  <div className="flex max-w-full w-[375px] flex-row items-start gap-1.5 max-md:justify-center">
                    <a href="..." className="text-neutral-800 text-base mt-px">
                      Ame
                    </a>
                    <div className="text-neutral-800 text-base max-w-[268px]">
                      rican Computer Science League (A
                    </div>
                    <a
                      href="..."
                      className="text-neutral-800 text-base self-stretch mt-px"
                    >
                      CSL)
                    </a>
                  </div>
                  <div className="flex max-w-full w-[326px] flex-row items-start gap-0 mt-2.5 max-md:justify-center">
                    <a
                      href="..."
                      className="text-neutral-800 text-base w-[169px]"
                    >
                      organizes computer
                    </a>
                    <a
                      href="..."
                      className="text-neutral-800 text-base w-[115px] self-stretch"
                    >
                      programming
                    </a>
                    <a href="..." className="text-neutral-800 text-base">
                      and c
                    </a>
                  </div>
                  <div className="text-neutral-800 text-lg max-w-[346px] mt-3.5">
                    schools, organizations and local groups
                  </div>
                  <div className="flex max-w-full w-[368px] flex-row items-start justify-between gap-5 mt-2">
                    <a
                      href="..."
                      className="text-neutral-800 text-base self-center"
                    >
                      will be our
                    </a>
                    <div className="flex flex-row items-start self-center gap-0 max-md:justify-center">
                      <a href="..." className="text-neutral-800 text-base">
                        . The 202
                      </a>
                      <a
                        href="..."
                        className="text-neutral-800 text-base mt-px"
                      >
                        3
                      </a>
                      <a
                        href="..."
                        className="text-neutral-800 text-base mt-px"
                      >
                        -20
                      </a>
                      <a
                        href="..."
                        className="text-neutral-800 text-base mt-px"
                      >
                        24
                      </a>
                      <a href="..." className="text-neutral-800 text-base">
                        school year
                      </a>
                    </div>
                  </div>
                  <div className="text-neutral-800 text-base max-w-[255px] mt-3">
                    ! Last year, about 8,000 students
                  </div>
                  <div className="text-neutral-800 text-base mt-2.5">
                    the United States, Canada, Europe, and Asia participated
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="text-neutral-800 text-base max-w-[1007px] ml-0 self-center mt-16 max-md:max-w-full">
            , providing an appropriate challenge for students of varying ages
            and abilities. An unlimited number of students may compete in
          </div>
          <div className="flex max-w-full w-[940px] ml-0 flex-row items-start self-center gap-0 mt-7 max-md:flex-wrap max-md:justify-center">
            <div className="text-neutral-800 text-base max-w-[515px] self-stretch max-md:max-w-full">
              Each season is divided into four contests, testing students on
            </div>
            <div className="text-neutral-800 text-base max-w-[357px] self-stretch">
              fundamental concepts in computer science
            </div>
            <a href="..." className="text-neutral-800 text-base self-stretch">
              , ranging
            </a>
          </div>
          <div className="text-neutral-800 text-base max-w-[862px] ml-16 mt-3 max-md:max-w-full max-md:ml-2.5">
            the upper divisions, each contest also includes a problem to solve
            by programming using Python, C++ or Java.
          </div>
          <div className="text-neutral-800 text-base max-w-[802px] ml-20 mt-12 max-md:max-w-full max-md:ml-2.5">
            ontests are administered online. Team advisors facilitate students’
            access to the online platform
          </div>
          <div className="flex max-w-full w-[1081px] flex-row items-start gap-4 ml-6 mt-2.5 max-md:flex-wrap max-md:justify-center max-md:ml-2.5">
            <img
              loading="lazy"
              srcSet="https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=100 100w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=200 200w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=400 400w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=800 800w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=1200 1200w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=1600 1600w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?&width=2000 2000w, https://cdn.builder.io/api/v1/image/assets/TEMP/d9853303-8f17-4c91-83c4-cb224e3a7a1c?"
              className="aspect-[1] object-contain object-center w-7 h-7 shrink-0 self-center mt-0.5"
            />
            <a href="..." className="text-neutral-800 text-base w-[134px] mt-7">
              Each topic on the
            </a>
            <a href="..." className="text-neutral-800 text-base w-[121px] mt-7">
              Study Materials
            </a>
            <div className="flex flex-col self-stretch max-md:max-w-full">
              <div className="flex max-w-full w-[664px] flex-row items-start gap-0 max-md:flex-wrap max-md:justify-center">
                <a href="..." className="text-neutral-800 text-base w-[136px]">
                  Online resources
                </a>
                <a href="..." className="text-neutral-800 text-base">
                  assist
                </a>
                <a href="..." className="text-neutral-800 text-base w-[165px]">
                  advisors to prepare
                </a>
                <div className="text-neutral-800 text-base max-w-[306px] self-stretch">
                  their students for each competition.
                </div>
              </div>
              <div className="flex max-w-full w-[620px] flex-row items-start gap-2.5 mt-2.5 max-md:flex-wrap max-md:justify-center">
                <div className="text-neutral-800 text-base max-w-[250px]">
                  page is linked to the page of the
                </div>
                <a href="..." className="text-neutral-800 text-base">
                  ACSL Wiki
                </a>
                <div className="text-neutral-800 text-base max-w-[257px] self-stretch">
                  that describes the topic in detail.
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="text-neutral-800 text-base max-w-[793px] ml-16 mt-3 max-md:max-w-full max-md:ml-2.5">
          At the end of the year, the top students are invited to compete in an
          online Finals competition.
        </div>
        <div className="max-w-full w-[1068px] self-center ml-1 mt-16">
          <div className="gap-5 flex max-md:flex-col max-md:items-stretch max-md:gap-0">
            <div className="flex flex-col items-stretch leading-[normal] w-[65%] max-md:w-full">
              <div className="flex flex-col mt-4 max-md:max-w-full max-md:mt-12">
                <div className="text-neutral-800 text-base max-md:max-w-full">
                  webinar is a great resource for prospective advisors,
                  students, and parents. It was prepared by Nathan Gorski, the
                  advisor of the
                </div>
                <a
                  href="..."
                  className="text-neutral-800 text-base ml-24 mt-5 max-md:ml-2.5"
                >
                  .
                </a>
              </div>
            </div>
            <div className="flex flex-col items-stretch leading-[normal] w-[35%] ml-5 max-md:w-full">
              <img
                loading="lazy"
                srcSet="https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=100 100w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=200 200w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=400 400w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=800 800w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=1200 1200w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=1600 1600w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?&width=2000 2000w, https://cdn.builder.io/api/v1/image/assets/TEMP/7248af4f-c697-4b2e-95cb-b1cc1400b406?"
                className="aspect-[1.89] object-contain object-center w-full max-md:mt-12"
              />
            </div>
          </div>
        </div>
        <div className="text-stone-900 uppercase text-4xl max-w-[531px] ml-16 mt-20 max-md:max-w-full max-md:ml-2.5">
          ACSL in KOREA, CHINA, and VIETNAM
        </div>
        <div className="text-neutral-800 text-base max-w-[854px] ml-16 mt-11 max-md:max-w-full max-md:ml-2.5">
          hina, or Vietnam, please read on for registration information;
          otherwise, use the form on this site to register.
        </div>
        <div className="flex max-w-full w-[997px] ml-0 flex-row items-start self-center gap-4 mt-12 max-md:flex-wrap">
          <div className="flex flex-col grow shrink-0 basis-auto mt-px">
            <div className="text-neutral-800 text-base">
              . Students participate in the regular season contests
            </div>
            <div className="text-neutral-800 text-base max-w-[329px] mt-2.5">
              reported in the ACSL leaderboard and top
            </div>
          </div>
          <div className="flex flex-col grow shrink-0 basis-auto max-md:max-w-full">
            <div className="flex max-w-full w-[444px] flex-row items-start gap-2.5 max-md:flex-wrap max-md:justify-center">
              <a href="..." className="text-neutral-800 text-base">
                , schools in
              </a>
              <a href="..." className="text-neutral-800 text-base mt-px">
                Korea
              </a>
              <a
                href="..."
                className="text-neutral-800 text-base w-[118px] self-stretch"
              >
                should register
              </a>
              <a
                href="..."
                className="text-neutral-800 text-base self-center -mt-px"
              >
                at
              </a>
              <a
                href="..."
                className="text-neutral-800 text-base w-[139px] self-stretch"
              >
                www.kcsl.acsl.org
              </a>
            </div>
            <div className="flex max-w-full w-72 flex-row items-start gap-0 mt-2.5 max-md:justify-center">
              <div className="text-neutral-800 text-base w-[198px] self-stretch">
                , translated into Korean
              </div>
              <a href="..." className="text-neutral-800 text-base mt-1">
                ;
              </a>
              <a
                href="..."
                className="text-neutral-800 text-sm self-center mt-px"
              >
                scores
              </a>
              <a
                href="..."
                className="text-neutral-800 text-base self-center mt-px"
              >
                are
              </a>
            </div>
          </div>
        </div>
        <div className="flex max-w-full w-[402px] flex-row items-start gap-0 ml-28 mt-2.5 max-md:justify-center max-md:ml-2.5">
          <a href="..." className="text-neutral-800 text-base w-[105px]">
            students are
          </a>
          <a href="..." className="text-neutral-800 text-base">
            invited to
          </a>
          <a href="..." className="text-neutral-800 text-base mt-px">
            ACSL's
          </a>{" "}
          <a
            href="..."
            className="text-neutral-800 text-base w-[147px] self-stretch"
          >
            end-of-year Finals
          </a>{" "}
          <a href="..." className="text-neutral-800 text-base self-center mt-1">
            .
          </a>
        </div>{" "}
        <div className="flex max-w-full w-[823px] flex-row items-start justify-between gap-5 ml-16 mt-6 max-md:flex-wrap max-md:ml-2.5">
          <div className="flex flex-row grow shrink-0 basis-auto items-start self-stretch gap-4 max-md:max-w-full max-md:flex-wrap">
            <div className="text-neutral-800 text-base max-w-[302px] grow shrink-0 basis-auto mt-px">
              e as individuals, and should register at
            </div>{" "}
            <div className="text-neutral-800 text-base max-w-[269px] grow shrink-0 basis-auto">
              to administer the ACSL contests in
            </div>
          </div>{" "}
          <div className="flex flex-row items-start self-stretch gap-0 max-md:justify-center">
            <a href="..." className="text-neutral-800 text-base">
              China
            </a>{" "}
            <a
              href="..."
              className="text-neutral-800 text-base self-center mt-1"
            >
              .
            </a>{" "}
            <a href="..." className="text-neutral-800 text-base">
              Students
            </a>{" "}
            <a href="..." className="text-neutral-800 text-base self-stretch">
              participat
            </a>
          </div>
        </div>{" "}
        <div className="flex max-w-full w-[884px] flex-row items-start self-center gap-0 ml-16 mt-2.5 max-md:flex-wrap max-md:justify-center">
          <div className="text-neutral-800 text-base max-w-[252px]">
            http://www.seedasdan.org/acsl
          </div>{" "}
          <a href="..." className="text-neutral-800 text-base">
            . Students
          </a>{" "}
          <div className="text-neutral-800 text-base max-w-[548px] self-stretch max-md:max-w-full">
            take the ACSL contests translated into Chinese, and top students
          </div>
        </div>{" "}
        <div className="text-neutral-800 text-base max-w-[443px] ml-16 mt-2.5 max-md:max-w-full max-md:ml-2.5">
          are invited to participate in ACSL's end-of-year Finals.
        </div>
        <div className="text-neutral-800 text-base max-w-[802px] ml-16 mt-7 max-md:max-w-full max-md:ml-2.5">
          . RICE administers the ACSL Contests to students as individuals,
          translating materials into Vietnamese.
        </div>
        <div className="flex max-w-full w-[740px] flex-row items-start gap-0 ml-16 mt-2.5 max-md:flex-wrap max-md:ml-2.5">
          <div className="flex flex-col grow shrink-0 basis-auto mt-px max-md:max-w-full">
            <div className="text-neutral-800 text-base max-w-[418px]">
              are invited to participate in ACSL's end-of-year Finals.
            </div>{" "}
            <div className="text-neutral-800 text-base max-w-[302px] mt-2.5">
              For more information, visit the RICE
            </div>
          </div>{" "}
          <div className="flex flex-col grow shrink-0 basis-auto">
            <div className="flex max-w-full w-[111px] flex-row items-start gap-0.5">
              <a href="..." className="text-neutral-800 text-base mt-px">
                T
              </a>{" "}
              <a href="..." className="text-neutral-800 text-base w-[100px]">
                op students
              </a>
            </div>{" "}
            <div className="flex max-w-full w-[213px] flex-row items-start gap-0 mt-2.5 max-md:justify-center">
              <a
                href="..."
                className="text-neutral-800 text-base w-[121px] self-stretch"
              >
                Facebook page
              </a>{" "}
              <a href="..." className="text-neutral-800 text-base self-center">
                or
              </a>{" "}
              <a href="..." className="text-neutral-800 text-base">
                website
              </a>{" "}
              <a
                href="..."
                className="text-neutral-800 text-base self-center mt-1"
              >
                .
              </a>
            </div>
          </div>
        </div>
      </div>{" "}
      <div className="flex max-w-full w-[1076px] flex-col self-center mt-16 mb-9 px-5">
        <img
          loading="lazy"
          srcSet="https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=100 100w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=200 200w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=400 400w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=800 800w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=1200 1200w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=1600 1600w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?&width=2000 2000w, https://cdn.builder.io/api/v1/image/assets/TEMP/ef7e59ae-939d-4246-9235-bf11e3ca4db2?"
          className="aspect-[1.53] object-contain object-center w-[708px] max-w-full self-center"
        />{" "}
        <div className="bg-rose-500 flex max-w-full w-[1076px] min-h-[3px] flex-col self-center mt-8" />{" "}
        <div className="flex max-w-full w-[1060px] flex-row items-start self-center justify-between gap-5 mt-11 max-md:flex-wrap">
          <div className="flex flex-row items-start self-stretch gap-0">
            <div className="text-neutral-800 text-base max-w-[395px] grow shrink-0 basis-auto">
              American Computer Science League © 1978-202
            </div>{" "}
            <a href="..." className="text-neutral-800 text-base mt-px">
              3
            </a>
          </div>{" "}
          <div className="flex flex-row items-start self-stretch gap-0 max-md:justify-center">
            <a
              href="..."
              className="text-neutral-800 text-right text-base w-[114px]"
            >
              Advisor Guide
            </a>{" "}
            <a href="..." className="text-neutral-800 text-right text-base">
              |
            </a>{" "}
            <a
              href="..."
              className="text-neutral-800 text-right text-base self-stretch mt-px"
            >
              FAQ
            </a>{" "}
            <a
              href="..."
              className="text-neutral-800 text-right text-base self-stretch"
            >
              |
            </a>{" "}
            <a
              href="..."
              className="text-neutral-800 text-right text-base mt-px"
            >
              Contact
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
