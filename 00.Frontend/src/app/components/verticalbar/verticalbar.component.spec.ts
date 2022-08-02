import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerticalbarComponent } from './verticalbar.component';

describe('VerticalbarComponent', () => {
  let component: VerticalbarComponent;
  let fixture: ComponentFixture<VerticalbarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VerticalbarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VerticalbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
