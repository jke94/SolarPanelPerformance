import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DatesDatepickerComponent } from './dates-datepicker.component';

describe('DatesDatepickerComponent', () => {
  let component: DatesDatepickerComponent;
  let fixture: ComponentFixture<DatesDatepickerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DatesDatepickerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DatesDatepickerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
