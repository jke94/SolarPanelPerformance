import { TestBed } from '@angular/core/testing';

import { DatesDatepickerService } from './dates-datepicker-service.service';

describe('DatesDatepickerService', () => {
  let service: DatesDatepickerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DatesDatepickerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
