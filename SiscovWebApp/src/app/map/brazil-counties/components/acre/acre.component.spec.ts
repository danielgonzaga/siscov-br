import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcreComponent } from './acre.component';

describe('AcreComponent', () => {
  let component: AcreComponent;
  let fixture: ComponentFixture<AcreComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AcreComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AcreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
